from django.shortcuts import render
from django.urls import reverse
from django.views import generic


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'content': 'This is a simple Django example rendering HTML.',
        'year': 2023
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'This is a simple Django example rendering HTML.',
        'year': 2023
    }
    return render(request, 'about.html', context)


def products(request):
    context = {
        'title': 'Products',
        'content': 'This is a simple Django example rendering HTML.',
        'year': 2023
    }
    return render(request, 'products.html', context)


def services(request):
    context = {
        'title': 'Services',
        'content': 'This is a simple Django example rendering HTML.',
        'year': 2023
    }
    return render(request, 'services.html', context)
