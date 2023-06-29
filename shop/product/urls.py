from django.urls import path, include
from . import views
from .views import add_to_cart, remove_from_card

app_name = 'products'

urlpatterns = [ 
    path('users/', include('users.urls') , name='users'),
    path('users/', include('users.urls'), name='users'),
    path('baskets/add/<int:product_id>/',
         add_to_cart, name='add_to_cart'),
    path('baskets/remove/<int:basket_id>/', remove_from_card, name='remove_from_card'),
    
]
