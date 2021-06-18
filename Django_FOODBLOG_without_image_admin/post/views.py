from django.shortcuts import render
from django.http.response import HttpResponse
from foodDB import foodData
from .models import PostTable

# Create your views here.
def getPost(request):
    foodInfo ={
        "foods" : foodData,
    }
    return render(request , template_name='post/post.html', context =foodInfo)

def getHome(request):
    admin= {
       "current_admin": "LAKSHE",
       "name" :"Food Blogs - 2021",
    }
    return render(request, template_name= 'post/home.html', context =admin)

def getIndex(request):
    posts =PostTable.objects.all()
    context ={
        "posts" : posts
    }
    return render(request, template_name= 'post/index.html', context =context)    

def getSinglePost(request, pk):
    post =PostTable.objects.get(id=pk)
    context ={
        "post" : post
    }
    return render(request , template_name= 'post/view-single-blog.html', context =context)    