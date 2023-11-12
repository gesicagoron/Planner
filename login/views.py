from django.shortcuts import render
from .models import Post

<<<<<<< HEAD

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'login/home.html', context)

=======
# Create your views here.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]



def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'login/home.html',context)
>>>>>>> 5090acacecee90c49bd8be207879b860ed4c97c7

def about(request):
    return render(request, 'login/about.html', {'title': 'About'})