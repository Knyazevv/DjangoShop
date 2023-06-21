from django.urls import path
from . import views
from users.views import (UserLoginView, register)


urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', register, name="register"),
]
