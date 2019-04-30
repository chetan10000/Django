from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Posts
# Create your views here.
def index(request):
    posts=Posts.objects.all()
    context={
        'title':'Latest Posts',
        'posts':posts
        
        }
    return render(request,'myapp/index.html',context)

def details(request,id):
    post=Posts.objects.get(id=id)
    context= {
           'post':post
                }
    return render(request,'myapp/details.html',context)