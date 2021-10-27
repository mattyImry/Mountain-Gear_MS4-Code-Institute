from django.test import TestCase
from .models import Review


class TestViews(TestCase):

    def test_add_review_page(self):

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_edit_review(self):
        review = Review.objects.create(review="new tent")
        response = self.client.get(f'/reviews/edit/{review.id}/12')
        self.assertEqual(response.status_code, 302)

    def test_delete_review(self):
        review = Review.objects.create(review="new tent")
        response = self.client.get(f'/reviews/delete/{review.id}')
        self.assertRedirects(response, '/products/12')
