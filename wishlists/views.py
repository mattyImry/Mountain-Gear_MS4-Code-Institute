from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile, Product, Wishlist, WishlistItem
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """
    View to display wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = user.wishlist.all()

    if wishlist:
        wishlist_items = WishlistItem.objects.filter(wishlist__in=wishlist)

    else:
        wishlist_items = []

    template = 'wishlists/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """
    view to add a product to wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    wishlist = Wishlist.objects.create(user=user)

    wishlist_item = WishlistItem.objects.create(wishlist=wishlist, product=product)
    wishlist_item.save()

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
    wishlist = wishlist = user.wishlist.all()
    wishlist_item = WishlistItem.objects.filter(product=product,
                                                wishlist__in=wishlist).delete()
    messages.success(request, f'Product {product.name} removed form wishlist!')
    return redirect(reverse('view_wishlist'))
