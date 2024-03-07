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

        if user.objects.filter(username=username).exists():
            return render(request,"register.html",{"error": "User already exists"})
        else:
            user = User.objects.create(username=username, password=password)
            user.save()
            return redirect("login")
    return render(request,"register.html")

def home(request):
    return render(request,"home.html")

def logoutPage(request):
    logout(request)
    return redirect("login")