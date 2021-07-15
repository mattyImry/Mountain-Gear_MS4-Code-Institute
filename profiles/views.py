from django.shortcuts import render


def profile(request):
    """
    display user's profile
    Code from Boutique Ado
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
