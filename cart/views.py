from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """
    View to render cart page
    """

    return render(request, 'cart/cart.html')
