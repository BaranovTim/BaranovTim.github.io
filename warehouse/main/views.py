from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News
from django.contrib.admin.models import LogEntry


def home(request):
    return render(request,'main/home.html')


def info(request):
    return render(request, 'main/info.html')


def news(request):
    news = News.objects.order_by('-date')
    return render(request,'main/news.html', {"news":news})



def profile(request):
    return render(request, 'main/profile.html')


def statistics(request):
    actions = LogEntry.objects.filter(user=request.user).order_by('-action_time')
    return render(request, 'main/statistics.html', {'actions': actions})
