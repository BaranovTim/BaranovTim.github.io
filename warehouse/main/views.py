from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import News

def home(request):
    return render(request,'main/home.html')


def info(request):
    return render(request, 'main/info.html')


def news(request):
    news = News.objects.order_by('-date')
    return render(request,'main/news.html', {"news":news})



def profile(request):
    return render(request, 'main/profile.html')


def statistics():
    return None
