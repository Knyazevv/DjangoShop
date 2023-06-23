from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='profile_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='profile_set', blank=True)

    def __str__(self):
        return self.user.username