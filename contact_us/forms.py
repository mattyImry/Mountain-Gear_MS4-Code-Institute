from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3, max_length=100, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Your email address'}), label='')

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message'}), label='')
