from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'login/home.html', context)


def about(request):
<<<<<<< HEAD
    return render(request, 'login/about.html', {'title': 'About'})
=======
    return HttpResponse('<h1>About</h1>')
>>>>>>> ee5acdddf3fd0a77fb772c0b80d37caf8af08ab6
