from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey(UserProfile, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    review = models.TextField()

    def __str__(self):
        return self.reviews
