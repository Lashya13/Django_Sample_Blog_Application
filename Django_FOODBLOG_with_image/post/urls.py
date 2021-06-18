

from django.urls import path
from django.urls.conf import include
from .import views



urlpatterns = [
  
    path('', views.getPost, name="post"),
    path('home/', views.getHome, name="home"),
]
