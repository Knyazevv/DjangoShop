from django.db import models

from django.shortcuts import render
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
# pip install psycopg2


class Category(models.Model):

    class Meta:
        db_table = "category"
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    
    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        db_table = "products"
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)



def __str__(self):
    return f"{self.name} {self.description} {self.price} {self.catedory}"


# @receiver(post_migrate)
# def populate_data(sender, **kwargs):
#     if sender.name == 'shop':
#         Category = apps.get_model('shop', 'Category')
#         Product = apps.get_model('shop', 'Product')
#         categories = [
#             {'name': 'Category 1', 'description': 'Description 1'},
#             {'name': 'Category 2', 'description': 'Description 2'},
#             {'name': 'Category 3', 'description': 'Description 3'},
#         ]

#         for category_data in categories:
#             category = Category(
#                 name=category_data['name'], description=category_data['description'])
#             category.save()
#         category_objects = Category.objects.all()

#         products = [

#             {'name': 'Product 1', 'description': 'Description 1',
#                 'price': 10.0, 'category': category_objects[0]},
#             {'name': 'Product 2', 'description': 'Description 2',
#                 'price': 20.0, 'category': category_objects[1]},
#             {'name': 'Product 3', 'description': 'Description 3',
#                 'price': 30.0, 'category': category_objects[2]},
#         ]

#         for product_data in products:
#             product = Product(
#                 name=product_data['name'],
#                 description=product_data['description'],
#                 price=product_data['price'],
#                 category=product_data['category']
#             )
#             product.save()
