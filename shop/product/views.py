from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def shop(request):
    return render(request, 'pages/shop.html')

def cart(request):
    return render(request, 'pages/cart.html')


def checkout(request):
    return render(request, 'product/checkout.html')


def contact(request):
    return render(request, 'product/contact.html')


def detail(request):
    return render(request, 'pages/detail.html')
