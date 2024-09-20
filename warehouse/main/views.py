from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import News, Warehouse_stock_deploy, QRScan_deploy

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
    actions = QRScan_deploy.QRScan_dep.objects.filter(scanned_by=request.user).order_by('-scanned_at')
    actions_all = QRScan_deploy.QRScan_dep.objects.order_by('-scanned_at')
    context = {
        'actions': actions,
        'actions_all': actions_all
    }
    return render(request, 'main/statistics.html', context)

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
        items = Warehouse_stock_deploy.Warehouse_stock_dep.objects.filter(item__name__icontains=query)
    else:
        # Если запрос не передан, отображаем все элементы
        items = Warehouse_stock_deploy.Warehouse_stock_dep.objects.order_by('quantity')

    return render(request, 'main/stock.html', {'items': items})

