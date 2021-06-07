from django.contrib import admin
from django.urls import path
from . import views


app_name = 'dcse'


urlpatterns = [

    path('', views.dcse_main, name="dcseMain"),

]
