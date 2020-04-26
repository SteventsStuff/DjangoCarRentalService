from django.shortcuts import render

from dummy_data import car_posts


def index(request):
    context = {
        'posts': car_posts,
        'title': 'kek'
    }
    return render(request, 'rental/index.html', context)


def about(request):
    context = {
        'posts': car_posts,
        'title': 'kek'
    }
    return render(request, 'rental/about.html', context)
