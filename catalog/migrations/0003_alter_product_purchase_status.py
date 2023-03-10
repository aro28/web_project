# Generated by Django 3.2 on 2023-03-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20230303_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_status',
            field=models.BooleanField(choices=[(True, 'Продан'), (False, 'Не продан'), (False, 'Зарезервирован'), (False, 'На складе'), (False, 'Товар в пути')], default=False, help_text='Пожалуйста выберите статус продуката', verbose_name='Статус продукта'),
        ),
    ]
