from django.shortcuts import render

# Create your views here.
def take(request):
    return render(request,'action_take/action_take.html')