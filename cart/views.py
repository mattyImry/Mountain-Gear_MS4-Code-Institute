from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """
    View to render cart page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add quantity of item to cart
    Code taken from Boutique Ado CI tutorial
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    number = None
    if 'product_size' or 'product_number' in request.POST:
        size = request.POST.get('product_size', None)
        number = request.POST.get('product_number', None)
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}

    elif number:
        if item_id in list(cart.keys()):
            if number in cart[item_id]['items_by_number'].keys():
                cart[item_id]['items_by_number'][number] += quantity
            else:
                cart[item_id]['items_by_number'][number] = quantity
        else:
            cart[item_id] = {'items_by_number': {number: quantity}}

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
