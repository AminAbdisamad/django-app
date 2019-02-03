from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Aminux',
        'title': 'Post One',
        'body': 'This is post one',
        'date': '03,Feb,2019'
    },
    {
        'author': 'abdihalim',
        'title': 'Post Two',
        'body': 'This is post Two',
        'date': '03,Feb,2019'
    },
    {
        'author': 'Hassan Adan',
        'title': 'Post Three',
        'body': 'This is post Three',
        'date': '03,Feb,2019'
    }
]


def home(request):
    context = {
        'posts': posts  # will loop using the key
    }
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')
