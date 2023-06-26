from django.contrib.auth.models import User
from users.models import CustomUser
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from users.forms import UserLoginForm
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from users.mixins import UserIsNotAuthenticated
from email.message import EmailMessage
import smtplib
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from users.models import Order_basket




User = get_user_model()


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = "Login"



class UserRegisterView(UserIsNotAuthenticated, CreateView):
   
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реєстрація на сайте'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # відправка листів з токеном
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('confirm_email', kwargs={
                                      'uidb64': uid, 'token': token})
        # current_site = Site.objects.get_current().domain
        current_site = f"127.0.0.1:8000/"
        # print(f"Activation URL: http://{current_site}{activation_url}")

        from_email = 'Confirmation of Registration <confirmationofregistration@ukr.net>'
        # to_email = 'Recipient Name <recipient_list>'
        to_email = [user.email]
        message_body = f'Пожалуйста, перейдите по следующей ссылке, чтобы подтвердить свой адрес электронной почты: http://{current_site}{activation_url}'

        msg = EmailMessage()
        msg['From'] = from_email
        msg['To'] = to_email
        msg.set_content(message_body)

        server = smtplib.SMTP_SSL('smtp.ukr.net', 2525)
        server.login("confirmationofregistration@ukr.net", "RxFucyKX5nqimoOk")
        server.send_message(msg)

        server.quit()

        # Перенаправлення користувача
        return redirect('email_confirmation_sent')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('email_confirmed')
        else:
            return redirect('email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Лист активації відправлено'
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'users/email_confirmed.html'
    
    def get_context_data(self, **kwargs):
        # Отримати екземпляр поточного користувача
        user = self.request.user
        
        # Оновити значення is_verifaild_email
        user.is_verified_email = True
        user.save()
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш емейл адрес активовано'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш емейл не активовано'
        return context



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, 'users/profile.html', {'form': form})


def seller_profile(request, id):
    seller = CustomUser.objects.get(id=id)

    context = {
        'seller': seller
    }

    return render(request, 'users/sellerprofile.html', context)



def add_to_cart(request):
    # Отримати необхідні дані з запиту POST
    user_id = request.POST.get('user_id')
    product_id = request.POST.get('product_id')

    # Отримати екземпляр CustomUser за допомогою ідентифікатора
    CustomUser = get_user_model()
    user = CustomUser.objects.get(id=user_id)

    # Зберегти дані у таблиці Order
    order = Order_basket(user=user, product_id=product_id)
    order.save()

    # Перенаправити користувача до іншої сторінки
    return redirect('/cart/')






