from django.shortcuts import render

from .models import Car


def index(request):
    context = {
        'posts': Car.objects.all(),
    }
    return render(request, 'rental/index.html', context)


def about(request):
    context = {
        'title': 'kek'
    }
    return render(request, 'rental/about.html', context)
