from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    photo_0 = models.ImageField(upload_to='users_image', null=True, blank=True)
    # photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_verified_email = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
