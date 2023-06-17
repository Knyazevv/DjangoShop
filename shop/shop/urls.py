from django.contrib import admin
from django.urls import path, include
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),     
    path('checkout/', views.checkout, name='checkout'), 
    path('contact/', views.contact, name='contact'), 
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('detail/<int:product_id>/', views.detail, name='detail'), 
    path('cart/', views.cart, name='cart'),
    path('products/', include('product.urls'))
]
