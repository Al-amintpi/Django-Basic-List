from django.contrib import admin
from django.urls import path, include
from QueryApp.views import *
from.import views

urlpatterns = [
       path('home_page/', views.index, name="home"),
]

