from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """
    View to render cart page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add quantity of item to cart
    Part of Code taken from Boutique Ado CI tutorial
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


def adjust_cart(request, item_id):
    """
    Adjust quantity of item into cart
    Part of Code taken from Boutique Ado CI tutorial
    """
    quantity = int(request.POST.get('quantity'))
    size = None
    number = None
    if 'product_size' or 'product_number' in request.POST:
        size = request.POST.get('product_size', None)
        number = request.POST.get('product_number', None)
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
    elif number:
        if quantity > 0:
            cart[item_id]['items_by_number'][number] = quantity
        else:
            del cart[item_id]['items_by_number'][number]

    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove quantity of item from cart
    Part of Code taken from Boutique Ado CI tutorial
    """
    try:
        size = None
        number = None
        if 'product_size' or 'product_number' in request.POST:
            size = request.POST.get('product_size', None)
            number = request.POST.get('product_number', None)
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
        elif number:
            del cart[item_id]['items_by_number'][number]
            if not cart[item_id]['items_by_number']:
                cart.pop(item_id)

        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
