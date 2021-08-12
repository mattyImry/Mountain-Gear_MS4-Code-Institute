from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile, Product, WishlistItem, Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """
    View to display wishlist
    """
    # product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=user)
    print(wishlist)
    template = 'wishlists/wishlist.html'
    context = {

        'wishlist': wishlist,
        # 'product': product,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    products = Wishlist.objects.get_or_create(products=product, user=user)
    #user = get_object_or_404(UserProfile, user=request.user)
    #wishlist = Wishlist(user=user, products=product)

    #wishlist.save()
    #print(product)
    #print(user)
    #print(wishlist)

    messages.success(
        request, f'Added {product.name} to your wishlist')
    product_id = product_id

    return redirect(reverse('view_wishlist'))


"""
@login_required
def delete_product_wishlist(request, product_id):
    
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist.delete(product)
    messages.success(request, 'Product removed form wishlist!')
    return redirect('wishlist')
"""
