

from django.urls import path
from django.urls.conf import include
from .import views



urlpatterns = [
  
    path('', views.getPost, name="post"),
    path('home/', views.getHome, name="home"),
    path('index/', views.getIndex, name="index"),
    path('single-blog/<str:pk>', views.getSinglePost, name="view-single-blog")

]
