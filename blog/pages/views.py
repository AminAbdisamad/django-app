from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()  # will loop using the key
    }
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')
