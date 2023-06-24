from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
