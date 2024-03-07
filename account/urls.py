from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginn,name="login"), #başlangıc konumunu login sayfası olarak ayarliyoruz.
    path("register/",views.register),
    path("home/",views.home,name="home"),
    path('logout/', views.logoutPage, name='logout'),
]