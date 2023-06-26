from django.shortcuts import render, get_object_or_404
from . models import Product, Category
from functools import wraps
from users.models import CustomUser, Order_basket




def context_data(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        products = Product.objects.order_by('name')
        categories = Category.objects.order_by('name')
        user = CustomUser.objects.order_by('username')
        user_id = Order_basket.objects.order_by('id')
        context = {
            "products": products,
            'categories': categories,
            'users': user,
            'user_id':user_id,
            
        }
        return func(request, *args, context=context, **kwargs)
    return wrapper



# def context_data(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         products = Product.objects.order_by('name')
#         categories = Category.objects.order_by('name')
#         user = CustomUser.objects.get(username=request.user.username)
#         user_id = Order_basket.objects.filter(user=user).first()
#         context = {
#             "products": products,
#             'categories': categories,
#             'user': user,
#             'user_id': user_id.id if user_id else None,
#         }
#         return func(request, *args, context=context, **kwargs)
#     return wrapper






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
def cart(request, context):   
   
    return render(request, 'pages/cart.html', context)

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