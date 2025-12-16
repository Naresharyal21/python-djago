from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myfirstapp/index.html')
def politics(request):
    return render(request,'myfirstapp/politics.html')