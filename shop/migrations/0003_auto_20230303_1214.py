# Generated by Django 3.2 on 2023-03-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230302_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена продукта'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='age',
            field=models.IntegerField(verbose_name='Возраст покупателя'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя покупателя'),
        ),
    ]