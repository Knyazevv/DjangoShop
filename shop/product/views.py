from django.shortcuts import render
from . models import  Product, Category

def index(request):
    products = Product.objects.order_by('name')
    
    context = {
        "products": products
    }
    return render(request, 'pages/index.html', context)


def shop(request):
    products = Product.objects.order_by('name')
    
    context = {
        "products": products
    }
    
    return render(request, 'pages/shop.html', context)

def cart(request):
    return render(request, 'pages/cart.html')


def checkout(request):
    return render(request, 'product/checkout.html')


def contact(request):
    return render(request, 'product/contact.html')


def detail(request):
    return render(request, 'pages/detail.html')
