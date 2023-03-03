from django.contrib import admin

# Register your models here.

from .models import Item, Purchase
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # item_list = ['name', 'price']
    list_display = ['name', 'price']
    search_fields = ['name', 'price', 'item__name', 'item__price']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'item']
    # purchase_list = ['name', 'age', 'item__name', 'item__price']
    search_fields = ['name', 'age', 'item__name', 'item_price']

