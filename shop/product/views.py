from django.shortcuts import render, get_object_or_404
from . models import Product, Category, Basket
from functools import wraps
from users.models import CustomUser
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



def context_data(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        products = Product.objects.order_by('name')
        categories = Category.objects.order_by('name')
        user = CustomUser.objects.order_by('username')

        paginator = Paginator(products, 20)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            "products": page,
            'categories': categories,
            'users': user,

        }
        return func(request, *args, context=context, **kwargs)
    return wrapper



@context_data
def index(request, context):
    return render(request, 'pages/index.html', context)

@context_data
def shop(request, context):
    return render(request, 'pages/shop.html', context)

@context_data
def checkout(request, context):
    return render(request, 'pages/checkout.html', context)

@context_data
def contact(request, context):
    return render(request, 'pages/contact.html', context)




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
