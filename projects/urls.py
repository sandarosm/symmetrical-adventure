from django.contrib import admin
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [

    path('',views.project_main, name="projectMain"),
    path('project_dete/',views.project_dete, name="projectDete"),
    path('project_dcse/', views.project_dcse, name="projectDcse"),


]
