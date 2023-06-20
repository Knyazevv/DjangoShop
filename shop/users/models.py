from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
