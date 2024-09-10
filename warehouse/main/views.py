from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import News
from qrcodes.models import Warehouse_stock
from django.contrib.admin.models import LogEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'main/home.html')

@login_required(login_url='profile')
def info(request):
    return render(request, 'main/info.html')

@login_required(login_url='profile')
def news(request):
    news = News.objects.order_by('-date')
    return render(request,'main/news.html', {"news":news})


def profile(request):
    return render(request, 'main/profile.html')

@login_required(login_url='profile')
def statistics(request):
    actions = LogEntry.objects.filter(user=request.user).order_by('-action_time')
    return render(request, 'main/statistics.html', {'actions': actions})
@login_required(login_url='profile')
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/add_user.html', {'form': form})


@login_required(login_url='profile')
def stock(request):
    query = request.GET.get('item')  # Получаем поисковый запрос

    if query:
        # Фильтруем элементы по имени (case-insensitive поиск)
        items = Warehouse_stock.objects.filter(item__name__icontains=query)
    else:
        # Если запрос не передан, отображаем все элементы
        items = Warehouse_stock.objects.order_by('quantity')

    return render(request, 'main/stock.html', {'items': items})

