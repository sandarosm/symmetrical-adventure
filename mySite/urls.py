"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from home import views as homepage_views

#from django.urls import include, re_path
urlpatterns = [
#    re_path(r'^admin/', admin.site.urls),
#    re_path(r'^articles/', include('articles.urls')),
#    re_path(r'^about/$', views.about),
#    re_path(r'^$', views.homepage),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('home/', include('home.urls')),
    path('dete/', include('dete.urls')),
    path('dcse/', include('dcse.urls')),
    path('projects/', include('projects.urls')),
    path('', homepage_views.homepage_view, name="Home"),



]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
