from django.contrib import admin
from django.urls import path
from . import views
#from django.urls import include, re_path

app_name = 'home'


urlpatterns = [

    #re_path(r'^$', views.article_list, name="list"),
    path('', views.homepage_view, name="homepageL"),
    path('homepage_faculty/', views.homepage_faculty, name="homeFaculty"),
    path('<title>/', views.news_detail, name="newsDetails"),
    #path('/', views.notice_view, name="noticeView")
    #path('notice_view/', views.notice_view, name="noticeView"),
    path('<title>/', views.notice_detail, name="noticeDetails"),



    #re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),


]
