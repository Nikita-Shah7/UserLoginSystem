from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('login',views.logIn,name="login"),
    path('welcome',views.welcome,name="welcome"),
    path('logOut',views.logOut,name="logOut"),
    # path('<str:nik>',views.notfound,name="notfound")
]
