from django.shortcuts import render, redirect
from qrcodes.models import QRScan

def quantity(request):
    last_scan = QRScan.objects.last()

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if 1 <= quantity <= 1000:
            last_scan.quantity = quantity
            last_scan.save()
            return redirect('home')

    return render(request, 'quantity/quantity.html', {'last_scan': last_scan})