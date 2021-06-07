from django.contrib import admin
from django.urls import path
from . import views


app_name = 'dete'


urlpatterns = [

    path('', views.dete_main, name="deteMain"),

]
