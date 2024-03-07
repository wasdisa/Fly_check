from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import UAVS


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

        if User.objects.filter(username=username).exists():
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

def add_sub(request):
    if request.method == "POST" :
        if request.POST["brand_name"] != " ":
            brand = request.POST["brand_name"]
            brand.save()
            return redirect("home")

        if request.POST["ammo_name"] != " ":
            ammo= request.POST["ammo_name"]
            ammo.save()
            return redirect("home")

        if request.POST["model_name"] != " ":
            model = request.POST["model_name"]
            model.save()
            return redirect("home")

    return render(request,"add_sub.html")

def uva_list(request):
    UVA = UAVS.objects.all() # Tüm nesneleri ID'ye göre sırala
    return render(request, 'uva_list.html', {'UVAS': UVA})

def add_uva(request):
    return render(request, 'add_auv.html')
