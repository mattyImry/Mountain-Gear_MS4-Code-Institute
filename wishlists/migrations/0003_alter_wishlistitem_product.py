# Generated by Django 3.2.4 on 2021-08-20 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_numbers'),
        ('wishlists', '0002_wishlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product'),
        ),
    ]
