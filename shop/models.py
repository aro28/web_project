from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название продукта')
    price = models.IntegerField(default=0, verbose_name='Цена продукта')

    def __str__(self):
        return f' Имя продукта: {self.name}, Цена продукта: {self.price}'

class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя покупателя')
    age = models.IntegerField(verbose_name='Возраст покупателя')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return f'Имя покупателя: {self.name}, - Возраст покупателя: {self.age}, Товар: {self.item}'
#on_delete=models.CASCADE: "Good bye world, I can't live without article_B" and commit suicide (this is the CASCADE behavior).