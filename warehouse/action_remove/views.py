from django.shortcuts import render

# Create your views here.
def remove(request):
    return render(request,'action_remove/action_remove.html')