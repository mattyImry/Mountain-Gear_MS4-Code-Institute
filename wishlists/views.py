from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile, Product, WishlistItem
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """
    View to display wishlist
    """
    wishlist = request.session.get('wishlist', {})

    products = []
    for i in wishlist:
        product = get_object_or_404(Product, pk=int(i))
        products.append(product)

    template = 'wishlists/wishlist.html'
    context = {
        'products': products,
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    wishlist = request.session.get('wishlist', {})
    wishlist[item_id] = item_id

    products = []
    for i in wishlist:
        item = get_object_or_404(Product, pk=int(i))
        products.append(item)

    request.session['wishlist'] = wishlist
    messages.success(
            request, f'Added {product.name} to your wishlist')

    template = 'wishlists/wishlist.html'
    context = {
        'products': products,
        'wishlist': wishlist,
    }
    return render(request, template, context)

"""
@login_required
def delete_product_wishlist(request, wishlistitem_id, product_id):
    
    wishlist_item = get_object_or_404(WishlistItem, pk=wishlistitem_id)
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item.delete()
    messages.success(request, 'Product removed form wishlist!')
    return redirect(reverse('wishlist'))
"""
