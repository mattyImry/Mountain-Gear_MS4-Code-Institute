from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_review_is_required(self):
        form = ReviewForm({'review': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review', form.errors.keys())
        self.assertEqual(form.errors['review'][0], 'This field is required.')

    def test_fields_explicit_form_meta(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ['review'])
