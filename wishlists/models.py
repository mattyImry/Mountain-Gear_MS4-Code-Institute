from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """
    Model to create a wishlist and wishlist item
    For credit please refer to readme
    for Slack post
    """
    user = models.ForeignKey(UserProfile, null=False, blank=False,
                             on_delete=models.CASCADE, related_name='wishlist')

    products = models.ForeignKey(Product, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='product', default=1)

    def __str__(self):
        return f'Wishlist ({self.user}) ({self.products})'
