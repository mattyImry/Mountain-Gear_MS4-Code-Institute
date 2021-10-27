from django.test import TestCase
from .models import Review



class TestModel(TestCase):

    def test_review_model(self):
        rev = Review.objects.create(review="sometxt")
