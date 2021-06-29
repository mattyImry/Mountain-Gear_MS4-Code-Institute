from django.shortcuts import render, \
     redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


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
    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(request,
                                 f'Update size {size.upper()} {product.name}'
                                 f' quantity to'
                                 f'{cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 f'Added size {size.upper()} {product.name}'
                                 f'to the cart!')

        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'Added size {size.upper()} {product.name}'
                             f'to the cart!')

    elif number:
        if item_id in list(cart.keys()):

            if number in cart[item_id]['items_by_number'].keys():
                cart[item_id]['items_by_number'][number] += quantity
                messages.success(request,
                                 f'Update number {number} {product.name}'
                                 f' quantity to '
                                 f' {cart[item_id]["items_by_number"]}')

            else:
                cart[item_id]['items_by_number'][number] = quantity
                messages.success(request,
                                 f'Added number {number} {product.name}'
                                 f' to the cart!')

        else:
            cart[item_id] = {'items_by_number': {number: quantity}}
            messages.success(request,
                             f'Added number {number} {product.name}'
                             f' to the cart!')

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name}'
                             f' quantity to {cart[item_id]}')

        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to the cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust quantity of item into cart
    Part of Code taken from Boutique Ado CI tutorial
    """
    product = get_object_or_404(Product, pk=item_id)
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
            messages.success(request,
                             f'Updated size'
                             f' {size.upper()} {product.name}'
                             f' quantity to'
                             f' {cart[item_id]["items_by_size"][size]}')

        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request,
                             f'Removed size {size.upper()} {product.name}'
                             f' from the cart!')

    elif number:
        if quantity > 0:
            cart[item_id]['items_by_number'][number] = quantity
            messages.success(request,
                             f'Update number {number} {product.name}'
                             f' quantity to '
                             f' {cart[item_id]["items_by_number"][number]}')

        else:
            del cart[item_id]['items_by_number'][number]
            if not cart[item_id]['items_by_number']:
                cart.pop(item_id)
            messages.success(request,
                             f'Removed number {number} {product.name}'
                             f' from the cart!')

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request,
                             f'Updated {product.name} to {cart[item_id]}')

        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} to the cart!')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove quantity of item from cart
    Part of Code taken from Boutique Ado CI tutorial
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
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
            messages.success(request,
                             f'Removed size {size.upper()} {product.name}'
                             f' from the cart!')

        elif number:
            del cart[item_id]['items_by_number'][number]
            if not cart[item_id]['items_by_number']:
                cart.pop(item_id)
            messages.success(request,
                             f'Removed number {number} {product.name}'
                             f' from the cart!')
            print(product)
        else:
            cart.pop(item_id)
        messages.success(request,
                         f'Removed {product.name} to the cart!')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting item: {e}')
        return HttpResponse(status=500)
