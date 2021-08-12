# Generated by Django 3.2.4 on 2021-08-12 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_numbers'),
        ('wishlists', '0003_auto_20210812_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='products',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product'),
        ),
    ]
