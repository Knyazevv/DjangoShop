from django.contrib import admin
from django.urls import path, include
from product import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:category_id>/',
         views.products_by_category, name='products_by_category'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('products/', include('product.urls')),
    path('users/', include('users.urls'), name='users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
