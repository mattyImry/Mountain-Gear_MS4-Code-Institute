# Generated by Django 3.2.4 on 2021-08-20 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_numbers'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_item', to='wishlists.wishlist')),
            ],
        ),
    ]
