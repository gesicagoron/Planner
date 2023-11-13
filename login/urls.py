from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='login'),
    path('about/', views.about, name='login-about'),
  
]
=======
    path('', views.home,name='login-home'),
    path('about/', views.about,name='login-about'),
]
>>>>>>> ee5acdddf3fd0a77fb772c0b80d37caf8af08ab6
