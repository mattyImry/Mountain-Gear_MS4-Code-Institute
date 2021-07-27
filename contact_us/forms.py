from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=3,
                           max_length=100, label='Name',
                           widget=forms.TextInput())

    email = email = forms.EmailField(widget=forms.EmailInput(),
                                     label='Your Email Address')

    message = forms.CharField(widget=forms.Textarea(), label='Message')
