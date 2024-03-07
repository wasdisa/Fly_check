from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginn,name="login"), #başlangıc konumunu login sayfası olarak ayarliyoruz.
    path("register/",views.register),
    path("home/",views.home,name="home"),
    path('logout/', views.logoutPage, name='logout'),
    path('add_sub/', views.add_sub, name='add_sub'),
    path('uva_list/', views.uva_list, name='uva_list'),
    path('add_auv/', views.add_uva, name='add_auv'),
]