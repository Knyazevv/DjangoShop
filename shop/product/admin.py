from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    list_editable = ('price',)
    list_per_page = 30
    search_fields = ('name', 'description', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('description',)
    list_per_page = 30


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)