from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Taken from Boutique Ado CI tutorial.
    Ordering list of product fields.
    """
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Taken from Boutique Ado CI tutorial.
    Ordering list of categoris fields.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
