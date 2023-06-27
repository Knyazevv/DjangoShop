from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import CustomUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Username'
    }))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username:
            raise forms.ValidationError("Username is required.")
        if not password:
            raise forms.ValidationError("Password is required.")

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


# class UserRegisterForm(UserCreationForm):
#     image = forms.ImageField(required=False)
#     is_verified_email = forms.BooleanField(required=False)
    
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(
#             attrs={"class": "form-control", "placeholder": "Enter email"}),
#     )
#     username = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={"class": "form-control", "placeholder": "Enter username..."}
#         ),
#     )
#     password1 = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "Enter password"}
#         ),
#     )
#     password2 = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "Confirm password"}
#         ),
#     )

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username', 'password1',
#                   'password2', 'image', 'is_verified_email', 'image')



class UserRegisterForm(UserCreationForm):
    image = forms.ImageField(required=False)
    is_verified_email = forms.BooleanField(required=False)
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter email"}
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username..."}
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1',
                  'password2', 'is_verified_email', 'image')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not email:
            raise forms.ValidationError("Email is required.")
        if not password1:
            raise forms.ValidationError("Password is required.")
        if not password2:
            raise forms.ValidationError("Please confirm your password.")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'image']



