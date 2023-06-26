from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission
from product.models import Product

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
        
        
class Order(models.Model):  
    class Meta:
        db_table = "orders"
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price =models.PositiveIntegerField(default=1)

        
    
        
        
class Order_basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "orders_basket"

    def delete_order_basket(self):
        self.delete()


  