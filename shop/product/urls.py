from django.urls import path, include
from . import views
from .views import add_to_cart, remove_from_card, increase_quantity, increase_quantity_minus

app_name = 'products'

urlpatterns = [ 
    path('users/', include('users.urls') , name='users'),
    # path('users/', include('users.urls'), name='users'),
    path('baskets/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('baskets/remove/<int:basket_id>/', remove_from_card, name='remove_from_card'),
    path('baskets/increase_quantity/<int:basket_id>/', increase_quantity, name='increase_quantity'),
    path('baskets/increase_quantity_minus/<int:basket_id>/', increase_quantity_minus, name='increase_quantity_minus'),

    
]

