from . models import Product, Category, Basket, UserHistory
from django.shortcuts import render, get_object_or_404, redirect
from functools import wraps
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from product.models import Basket
from email.message import EmailMessage
import smtplib
from django.db.models import Q
from django.db.models import  Sum
from .models import ContactFormEntry
from django.urls import reverse
from .models import Product

from django.contrib.auth.views import LogoutView


def context_data(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        
        search_query = request.GET.get('search', '')
        products = Product.objects.order_by('name')

        total_product_quantity = products.aggregate(total_product_quantity=Sum('quantity'))['total_product_quantity'] or 0

        if search_query:
            products = products.filter(Q(name__icontains=search_query) | Q(category__name__icontains=search_query))
        else:
            price_from = request.GET.get('price_from')
            price_to = request.GET.get('price_to')

            if price_from and price_to:
                try:
                    price_from = float(price_from)
                    price_to = float(price_to)
                    products = products.filter(price__gte=price_from, price__lte=price_to)
                except ValueError:
                  
                    error_message = "Введіть коректні числові значення для ціни."
                 
                    return HttpResponse(error_message)
            
            
            
        categories = Category.objects.order_by('name')
        baskets = Basket.objects.filter(user=user)
        total_quantity = baskets.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        total_sum = sum(basket.sum() for basket in baskets)

      
        sort_by_price = request.GET.get('sort_price')
        if sort_by_price == 'asc':
            products = products.order_by('price')
        elif sort_by_price == 'desc':
            products = products.order_by('-price')

    
        product_counts = Product.get_product_count_in_price_ranges()

        paginator = Paginator(products, 20)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        user_histories = UserHistory.objects.all()
        context = {
            "products": page,
            'categories': categories,
            'users': user,
            'baskets': baskets,
            'total_sum': total_sum,
            'total_quantity': total_quantity,
            'search_query': search_query,
            'total_product_quantity': total_product_quantity,
            'product_counts': product_counts, 
            'user_histories': user_histories,
        }

        return func(request, *args, context=context, **kwargs)

    return wrapper


@context_data
def checkout(request, context):
    if request.method == 'POST':        
        user = request.user
        baskets = Basket.objects.filter(user=user)
        
        products = [basket.product.name for basket in baskets]
        basket_sums = [basket.sum() for basket in baskets]       
        total_sum = sum(basket_sums)
        
               
        from_email = 'Замовлення товару <confirmationofregistration@ukr.net>'
        to_email = [user.email]
        
        message_body = ''
        for product, basket_sum in zip(products, basket_sums):
            message_body += f'Product : {product} Sum: {basket_sum}\n'
        message_body += f'\nTotal Sum: {total_sum}'
        
        msg = EmailMessage()
        msg['From'] = from_email
        msg['To'] = to_email
        msg.set_content(message_body)

        server = smtplib.SMTP_SSL('smtp.ukr.net', 2525)
        server.login("confirmationofregistration@ukr.net", "RxFucyKX5nqimoOk")
        server.send_message(msg)

        server.quit()
        baskets.delete()
        return redirect('index')
    
    return render(request, 'pages/checkout.html', context)


def detail_view(request, product_id):
    user = request.user
    UserHistory.create_or_update(product_id, user)
    url = reverse('detail', args=[product_id])
    return redirect(url)




@context_data
def index(request, context):
    return render(request, 'pages/index.html', context)


@context_data
def shop(request, context):
 
    return render(request, 'pages/shop.html', context)


@context_data
def products_by_category(request, category_id, context):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category).order_by('name')
    categories = Category.objects.order_by('name')
    
    context = {
        'category': category,
        'categories':categories,
        'products': products,
    }
    return render(request, 'pages/products_by_category.html', context)


@context_data
def detail(request, product_id ,context):
    products = get_object_or_404(Product, id=product_id)      
    categories = Category.objects.order_by('name')
    context = {       
        'categories':categories,
        'products': products,
    }
    return render(request, 'pages/detail.html', context)


@login_required
def cart(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = 0

    for basket in baskets:
        total_sum += basket.sum()

    context = {
        'baskets': baskets,
        'total_sum': total_sum,
    }
    return render(request, 'pages/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_card(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def increase_quantity(request, basket_id):
        basket = Basket.objects.get(id=basket_id)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def increase_quantity_minus(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.quantity -= 1
    if basket.quantity == 0:
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])



# @context_data
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
        entry = ContactFormEntry(name=name, email=email, subject=subject, message=message)        
        try:
            entry.save()
        except Exception as e:          
            print(e)        
        return redirect('index')    
    return render(request, 'pages/contact.html')


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):      
        user = request.user
        UserHistory.objects.filter(user=user).delete()
        return super().dispatch(request, *args, **kwargs)








# def context_data(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         products = Product.objects.order_by('name')
#         categories = Category.objects.order_by('name')
#         user = CustomUser.objects.order_by('username')     

#         baskets = []  

#         if request.user.is_authenticated:  
#             baskets = Basket.objects.filter(user=request.user)

#         paginator = Paginator(products, 2)
#         page_number = request.GET.get('page')
#         page = paginator.get_page(page_number)        
        
#         user = request.user if request.user.is_authenticated else None

#         if user:
#             total_quantity = Basket.objects.filter(user=user).aggregate(total_quantity=models.Sum('quantity'))['total_quantity']
#         else:
#             total_quantity = 0

#         total_sum = 0
#         for basket in baskets:
#             total_sum += basket.sum()

#         # baskets = Basket.objects.filter(user=request.user)
        
        
#         search_query = request.GET.get('search', '')

#         if search_query:
#          products = Product.objects.filter(
#             Q(name__icontains=search_query) | Q(category__name__icontains=search_query)
#         )
#         else:
#            products = Product.objects.all()

#         context = {
#             "products": page,
#             'categories': categories,
#             'users': user,
#             'baskets': baskets,
#             'total_sum': total_sum,
#             'total_quantity': total_quantity,
#             'search_query': search_query,
#             'products': products,

#         }
#         return func(request, *args, context=context, **kwargs)
#     return wrapper


# ПРАЦЮЄ

# def context_data(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         user = request.user if request.user.is_authenticated else None
        
#         search_query = request.GET.get('search', '')
#         products = Product.objects.order_by('name')

#         total_product_quantity = products.aggregate(total_product_quantity=Sum('quantity'))['total_product_quantity'] or 0

#         if search_query:
#             products = products.filter(Q(name__icontains=search_query) | Q(category__name__icontains=search_query))

#         categories = Category.objects.order_by('name')
#         baskets = Basket.objects.filter(user=user)
#         total_quantity = baskets.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
#         total_sum = sum(basket.sum() for basket in baskets)

#         paginator = Paginator(products, 20)
#         page_number = request.GET.get('page')
#         page = paginator.get_page(page_number)

#         context = {
#             "products": page,
#             'categories': categories,
#             'users': user,
#             'baskets': baskets,
#             'total_sum': total_sum,
#             'total_quantity': total_quantity,
#             'search_query': search_query,
#             'total_product_quantity': total_product_quantity,
#         }

#         return func(request, *args, context=context, **kwargs)

#     return wrapper