from django.shortcuts import render, \
     get_object_or_404, get_list_or_404
from django.contrib import messages
from .models import UserProfile, Product


def view_wishlist(request):
    """
    View to display wishlist
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = request.session.get('wishlist', {})
    template = 'wishlists/wishlist.html'
    context = {
        'wishlist': wishlist,
        'profile': profile,
    }

    return render(request, template, context)