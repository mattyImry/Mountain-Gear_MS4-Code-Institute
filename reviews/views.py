from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, UserProfile, Review
from .forms import ReviewForm


@login_required
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


@login_required
def edit_review(request, review_id, product_id):
    """
    View to edit review
    """
    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'You updated your review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update your review!\
                                     Please try again.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.review}')
    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id, product_id):
    """
    View to delete review
    """
    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.get(pk=product_id)

    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
