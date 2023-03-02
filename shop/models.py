from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
#on_delete=models.CASCADE: "Good bye world, I can't live without article_B" and commit suicide (this is the CASCADE behavior).