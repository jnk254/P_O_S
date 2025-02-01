

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'index.html')

def login(request):
    return render (request,'login.html')

def resetpassword(request):
    return render (request,'password.html')

def register(request):
    return render (request,'register.html')

