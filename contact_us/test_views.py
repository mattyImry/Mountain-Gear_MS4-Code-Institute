from django.test import TestCase


class TestViews(TestCase):

    def test_contact_us(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')
