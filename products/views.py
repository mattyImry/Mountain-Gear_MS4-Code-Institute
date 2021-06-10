from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):

    """
    View to render products and search functionality
    Code taken from Boutique Ado CI tutorial
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
