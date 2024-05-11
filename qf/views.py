from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hellow, world")

def home(request):
    return render(request,'qf/home.html')
def login(request):
    return render(request,'qf/login.html')
