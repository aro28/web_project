from django.contrib import admin

# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    # name_list = ['name']
    list_display = ['name',]
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    # product_list = ['name', 'price', 'date']
    list_display = ['name', 'price', 'date', 'purchase_status',]
    search_fields = ['name', 'price', 'category__name', 'purchase_status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
