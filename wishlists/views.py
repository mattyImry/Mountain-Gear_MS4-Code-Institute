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
    view to add to wishlist
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
    View to delete wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(products=product, user=user).delete()

    messages.success(request, 'Product removed form wishlist!')
    return redirect(reverse('view_wishlist'))
