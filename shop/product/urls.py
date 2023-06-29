from django.urls import path, include
from . import views
from .views import add_to_cart

app_name = 'products'

urlpatterns = [ 
    path('users/', include('users.urls') , name='users'),
    path('users/', include('users.urls'), name='users'),
    path('baskets/add/<int:product_id>/',
         add_to_cart, name='add_to_cart'),
    
]
