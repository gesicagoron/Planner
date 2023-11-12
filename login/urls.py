from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='login-home'),
    path('about/', views.about,name='login-about'),
]