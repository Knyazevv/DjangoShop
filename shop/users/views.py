from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from users.forms import UserLoginForm
from .forms import UserCreationForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = "Login"


# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("index")
#     else:
#         form = UserCreationForm()
#     context = {"form": form}
#     return render(request, "users/register.html", context)


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'
    success_message = 'Вы успішно зареєструвались!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реєстрація'
        return context
