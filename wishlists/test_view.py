from django.test import TestCase
from .models import Wishlist

class TestViews(TestCase):

    def test_get_wishlist_page(self):

        response = self.client.get('/wishlists/')
        self.assertEqual(response.status_code, 302)

    def test_add_wishlist(self):

        response = self.client.post('/wishlists/', {'wishlist':'Testing'})
        self.assertRedirects(response, '/accounts/login/?next=/wishlists/')

