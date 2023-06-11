from django.shortcuts import render


def index(request):
    return render(request, 'product/index.html')


def shop(request):
    return render(request, 'product/shop.html')

def cart(request):
    return render(request, 'product/cart.html')


def checkout(request):
    return render(request, 'product/checkout.html')


def contact(request):
    return render(request, 'product/contact.html')


def detail(request):
    return render(request, 'product/detail.html')
