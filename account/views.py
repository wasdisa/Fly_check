from django.shortcuts import render,HttpResponse,redirect


# Create your views here.

def loginn(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")