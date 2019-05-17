# blog/views.py
from django.shortcuts import render

posts = [
    {
        'author': 'Ingrid M',
        'title': 'Blog Post 1',
        'content': '1st post content',
        'date_posted': 'April 13, 2019',
    },
    {
        'author': 'Le Maurien',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'date_posted': 'May 17, 2019',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})