from django.urls import path
from .views import UserLoginView, UserRegisterView, EmailConfirmationSentView, UserConfirmEmailView, EmailConfirmedView,\
    EmailConfirmationFailedView
from django.contrib.auth import views as auth_views
from .views import profile, seller_profile




urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("profile/", profile, name="profile"),
    path("sellerprofile/<int:id>/", seller_profile, name="sellerprofile"),
    path('profile', profile, name='profile'),  
    # path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    
]

