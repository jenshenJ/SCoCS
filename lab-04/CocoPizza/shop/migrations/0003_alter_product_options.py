# Generated by Django 4.0.4 on 2023-06-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]