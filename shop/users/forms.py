from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control','placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control','placeholder': 'Password', type :'Password'
    }))
class Meta:
    model = User
    fields =('username', 'password')

