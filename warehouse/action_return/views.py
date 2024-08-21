from django.shortcuts import render

# Create your views here.
def return_back(request):
    return render(request,'action_return/action_return.html')