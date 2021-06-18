from django.shortcuts import render
from django.http.response import HttpResponse
from foodDB import foodData

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
    