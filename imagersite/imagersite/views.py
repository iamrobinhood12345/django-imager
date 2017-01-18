from django.shortcuts import render


def home_page(request, *args, **kwargs):
    return render(request, template_name='home.html') 