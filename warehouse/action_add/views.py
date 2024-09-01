from django.shortcuts import render
from qrcodes.models import Warehouse_stock, Item
from qrcodes.models import QRScan

# Create your views here.
def add(request):
    QRScan.objects.create(action = 'added')
    return render(request,'action_add/action_add.html')