from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    return render(request,'blog/index.html')


def buisness(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/buisness.html',context)

def sports(request):
    return render(request,'blog/sports.html')

def enter(request):
    return render(request,'blog/enter.html')

def our(request):
    return render(request,'blog/our.html')







# Create your views here.
