from django.shortcuts import render
from . models import Product, Category
from functools import wraps



def context_data(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        products = Product.objects.order_by('name')
        categories = Category.objects.order_by('name')
        context = {
            "products": products,
            'categories': categories
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
def cart(request, context):
    return render(request, 'pages/cart.html', context)

@context_data
def checkout(request, context):
    return render(request, 'pages/checkout.html', context)

@context_data
def contact(request, context):
    return render(request, 'pages/contact.html', context)

@context_data
def detail(request, context):
    return render(request, 'pages/detail.html', context)
