from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm

import os


def contact_us(request):
    """
    View to submit contact form for contact_us.html
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        user_email = request.POST.get('email')
        if form.is_valid():

            email = EmailMessage(
                'Subject',
                'Message',
                os.environ.get("EMAIL"),
                [os.environ.get("EMAIL")],
                reply_to=[user_email],)

            try:
                email.send(fail_silently=False) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact_us'))
        else:
            messages.error(request, 'Message not sent please try again.')
    else:
        form = ContactForm()

    template = 'contact_us/contact_us.html'
    context = {
        'form': form,

    }

    return render(request, template, context)
