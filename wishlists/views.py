from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile, Product, Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """
    View to display wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=user)
    template = 'wishlists/wishlist.html'
    context = {

        'wishlist': wishlist,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """
    view to add a product to wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    products = Wishlist.objects.get_or_create(products=product, user=user)

    messages.success(
        request, f'Added {product.name} to your wishlist')

    return redirect(reverse('view_wishlist'))


@login_required
def delete_product_wishlist(request, product_id):

    """
    View to delete a product from wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(products=product, user=user).delete()

    print(product.id)
    print(user)
    print(wishlist)
    messages.success(request, f'Product {product.name} removed form wishlist!')
    return redirect(reverse('view_wishlist'))
