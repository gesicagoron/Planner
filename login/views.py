from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.shortcuts import get_object_or_404

def home(request):
    context = {
        # You can add any additional context data for the home page here
    }
    return render(request, 'login/home.html', context)


def destinations(request):
    context = {
        # You can add any additional context data for the home page here
    }
    return render(request, 'login/destinations.html', context)


def post(request):
    posts_with_likes = Post.objects.annotate(like_count=Count('likes'))

    context = {
        'posts': Post.objects.all()
        
    }
    return render(request, 'login/post.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'login/post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.all()  


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['like_count'] = post.likes.count()
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'login/about.html', {'title': 'About'})


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post-detail', pk=pk)

def task_list(request):
    return render(request, 'login/task_list.html', {'title': 'Tasks'})