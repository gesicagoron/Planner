from django.urls import path
from .views import (
    home,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
     like_post
)
from . import views

urlpatterns = [
    path('', home, name='login-home'),  
    path('', PostListView.as_view(), name='login-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='login-about'),
    path('post/<int:pk>/like/', like_post, name='like-post'),
    path('posts/', PostListView.as_view(), name='login-post'), 


]
