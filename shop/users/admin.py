from django.contrib import admin
from users.models import User

admin.site.register(User)

class UserAdmin(User):
    list_display = ('username')