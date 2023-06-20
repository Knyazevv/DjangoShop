from django.shortcuts import render
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    title = "Login"

class UserRegisterView(LoginView):
    template_name = 'users/register.html'
    title = "Register"
