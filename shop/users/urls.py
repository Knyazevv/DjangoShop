from django.urls import path
from . import views
from users.views import (UserLoginView, UserRegisterView)


# http://127.0.0.1:8000/users/register/
# http://127.0.0.1:8000/users/login/


urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', UserRegisterView.as_view(), name="login"),
]
