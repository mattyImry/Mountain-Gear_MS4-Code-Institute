from django.test import TestCase
from django.core import mail


class TestViews(TestCase):

    def test_contact_us(self):
        """Testing http response and template"""

        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')

    def test_send_email(self):

        """Testing Send message."""
        mail.send_mail(
            'subject', 'user_message',
            'mountaingear@gear.com', ['to@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'subject')
