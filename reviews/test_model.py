from django.test import TestCase
from .models import Review, UserProfile, Product
from django.shortcuts import get_object_or_404


class TestModel(TestCase):

    def test_review_model(self):
        rev = Review.objects.create(review="sometxt")
        
    
