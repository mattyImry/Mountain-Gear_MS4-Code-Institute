from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from reviews.forms import ReviewForm

# Create your views here.


def all_products(request):

    """
    View to render products and search functionality
    Code taken from Boutique Ado CI tutorial
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No product added to search box")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)

            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    """
    View to render product detail
    Code taken from Boutique Ado CI tutorial
    """
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(request.POST)
    reviews = product.reviews.all()
    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    View to add product to website
    Code taken from Boutique Ado CI tutorial
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do this action')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.\
                            Please fill in form correctly.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to edit product to website
    Code taken from Boutique Ado CI tutorial
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do this action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to uodate product.\
                            Please fill in form correctly.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View to delete product from website
    Code taken from Boutique Ado CI tutorial
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do this action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
