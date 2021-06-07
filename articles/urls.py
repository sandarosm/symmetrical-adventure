from django.contrib import admin
from django.urls import path
from . import views
#from django.urls import include, re_path

app_name = 'articles'


urlpatterns = [

    #re_path(r'^$', views.article_list, name="list"),
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('<slug>/', views.article_detail, name="detail"),
    #re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),


]
