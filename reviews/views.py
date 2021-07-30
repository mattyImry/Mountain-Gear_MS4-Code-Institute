from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib import messages
from .models import Product, UserProfile
from .forms import ReviewForm


def add_review(request, product_id):
    """
    view to add review to product
    Code from Slack please refer to read me for credit
    """
    product = Product.objects.get(pk=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            product = Product.objects.get(pk=product_id)
            profile = UserProfile.objects.get(user=request.user)
            review.product = product
            review.profile = profile
            review.save()
            messages.success(request, 'Successfully added your review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Fail to upload review. Please try again')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
