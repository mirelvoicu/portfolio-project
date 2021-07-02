from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def blog_home(request):
    posts = Post.objects
    return render(request,'blog/home.html',{'posts':posts})

def detail(request,blog_id):

    detailblog=get_object_or_404(Blog, pk=blog_id) #get particular object from database or return 404

    return render(request,'blog/detail.html',{'detailblog':detailblog})

