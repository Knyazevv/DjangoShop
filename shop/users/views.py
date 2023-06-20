from django.shortcuts import render
from django.contrib.auth.views import LoginView
from users.forms import UserLoginForm

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = "Login"

class UserRegisterView(LoginView):
    template_name = 'users/register.html'
    title = "Register"
