from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name="product"),
    # path('<int:product_id>/', views.product, name="product"),
    # path("search", views.search, name="name")
    path('users/', include('users.urls') , name='users'),
]
