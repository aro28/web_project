from django.db import models
from datetime import datetime, date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название категории')
    def __str__(self):
        return f' Category name: {self.name}'

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название продукта', help_text="Пожалуйста укажите имя продукта")
    price = models.IntegerField(default=0, verbose_name='Цена продукта', help_text="Цена указана в сомах")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Пожалуйста выберите категорию продукта")
    purchase_status = models.BooleanField(default=False, verbose_name='Статус продукта', help_text="Пожалуйста выберите статус продуката",choices=(
                                            (True, "Продан"),
                                            (False, "Не продан"),
                                            (False, "Зарезервирован"),
                                            (False, "На складе"),
                                            (False, "Товар в пути")
                                            ))
    date = models.DateField(default=date.today, verbose_name='Дата покупки продукта', help_text="Укажите дату покупки продукта")

    def __str__(self):
        return f' Category: {self.category.name}, Product: {self.name} - price: {self.price} - purchase date: {self.date},' \
               f' Доступность: {self.purchase_status}'
