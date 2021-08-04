from django.shortcuts import render, \
     get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from .models import UserProfile, Product


def view_wishlist(request):
    """
    View to display wishlist
    """
    wishlist = request.session.get('wishlist', {})
    template = 'wishlists/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    print(wishlist)

    return render(request, template, context)


def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', '0'))

    wishlist = request.session.get('wishlist', {})
    wishlist[item_id] = quantity

    request.session['wishlist'] = wishlist
    messages.success(
            request, f'Added {product.name} to your wishlist')
    return redirect('product_detail', product_id=item_id)


    # if item_id in list(wishlist.keys()):
    #     wishlist[item_id] += quantity
             
    #     messages.success(request, f'Updated {product.name}\
    #                              quantity to {wishlist[item_id]}')
    # else:
    #     wishlist[item_id] = quantity
    #     print(wishlist)
    #     messages.success(request, f'Added {product.name} to your wishlist')

    # print(wishlist)

    

    # if request.method == 'POST':
    #     print("POST")

    # product = get_object_or_404(Product, pk=item_id)
    # quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
  
    # size = None
    # number = None

    # if 'product_size' or 'product_number' in request.POST:
    #     size = request.POST.get('product_size', None)
    #     number = request.POST.get('product_number', None)

    # wishlist = request.session.get('wishlist', {})

    # if size:
    #     if item_id in list(wishlist.keys()):

    #         if size in wishlist[item_id]['items_by_size'].keys():
    #             wishlist[item_id]['items_by_size'][size] += quantity
    #             messages.success(request,
    #                              f'Update size {size.upper()} {product.name}'
    #                              f' quantity to'
    #                              f'{wishlist[item_id]["items_by_size"][size]}')        
    #         else:
    #             wishlist[item_id]['items_by_size'][size] = quantity
    #             messages.success(request,
    #                              f'Added size {size.upper()} {product.name}'
    #                              f'to the wishlist!')

    #     else:
    #         wishlist[item_id] = {'items_by_size': {size: quantity}}
    #         messages.success(request,
    #                          f'Added size {size.upper()} {product.name}'
    #                          f'to the wishlist!')

    # elif number:
    #     if item_id in list(wishlist.keys()):

    #         if number in wishlist[item_id]['items_by_number'].keys():
    #             wishlist[item_id]['items_by_number'][number] += quantity
    #             messages.success(request,
    #                              f'Update number {number} {product.name}'
    #                              f' quantity to '
    #                              f' {wishlist[item_id]["items_by_number"]}')

    #         else:
    #             wishlist[item_id]['items_by_number'][number] = quantity
    #             messages.success(request,
    #                              f'Added number {number} {product.name}'
    #                              f' to the wishlist!')

    #     else:
    #         wishlist[item_id] = {'items_by_number': {number: quantity}}
    #         messages.success(request,
    #                          f'Added number {number} {product.name}'
    #                          f' to the wishlis!')

    # else:
    #     if item_id in list(wishlist.keys()):
    #         wishlist[item_id] += quantity
    #         messages.success(request,
    #                          f'Updated {product.name}'
    #                          f' quantity to {wishlist[item_id]}')

    #     else:
    #         wishlist[item_id] = quantity
    #         messages.success(request, f'Added {product.name} to the wishlist!')

    # print("Wishlist", wishlist)
    # request.session['wishlist'] = wishlist
    # return redirect(redirect_url)
