from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),     
    path('cart/', views.cart, name='cart'),
    path('detail/', views.detail, name='detail'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('contact/', views.contact, name='contact'), 

]
