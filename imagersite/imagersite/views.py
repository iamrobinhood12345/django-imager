from django.shortcuts import render


def home(request):
    """The home view directs here."""
    return render(request, 'base.html')
