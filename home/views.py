from django.shortcuts import render, redirect
from .models import newsUpdate
from .models import noticeUpdate
from django.http import HttpResponse


# Create your views here.

def homepage_faculty(request):
    return render(request, "home/faculty.html")

def homepage_view(request):
    news = newsUpdate.objects.all().order_by('date')
    return render(request, "home/homepage.html",{'news':news})

def news_detail(request, title):
    newsDetail = newsUpdate.objects.get(title=title)
    return render(request, 'home/homeNews.html',{'newsDetail':newsDetail})


#to be Configure
def notice_view(request):
    notice = noticeUpdate.objects.all().order_by('date')
    return render(request, "home/homepage.html", {'notice':notice})

def notice_detail(request, title):
    noticeDetail = noticeUpdate.objects.get(title=title)
    return render(request, 'home/homeNotice.html', {'noticeDetail':noticeDetail})
