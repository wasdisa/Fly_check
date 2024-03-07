from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def loginn(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html',{"error": "Invalid username or password"})
        
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

    return render(request,"register.html")

def home(request):
    return render(request,"home.html")

def logoutPage(request):
    logout(request)
    return redirect("login")