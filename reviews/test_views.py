from django.test import TestCase
#from .models import Review


class TestViews(TestCase):

    def test_add_review_page(self):

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

