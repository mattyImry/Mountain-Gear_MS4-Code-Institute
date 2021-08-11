from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile, Product, WishlistItem, Wishlist
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

    user = get_object_or_404(UserProfile, user=request.user)

    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist(user=user, products=product)


    wishlist.save()
    messages.success(
        request, f'Added {product.name} to your wishlist')
    
    template = 'wishlists/wishlist.html'
    context = {
        'product': product,
        'wishlist': wishlist,
        
    }
    return redirect('view_wishlist')


"""
@login_required
def delete_product_wishlist(request, product_id):
    
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist.delete(product)
    messages.success(request, 'Product removed form wishlist!')
    return redirect('wishlist')
"""
