from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """
    View to create contact form for contact_us.html
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
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
