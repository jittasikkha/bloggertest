"""lpmpblogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django import urls
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from downloadapp.views import download
from profiles.views import profile
from django.conf import settings
from django.urls import re_path as url
from django.views.static import serve

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', include(('cmsapp.urls'))),
    path('profile',include('profiles.urls')),
    path('',include('downloadapp.urls')),
    url(r'^download/(?P<path>.*)$' , serve, {'document_root' : settings.MEDIA_ROOT}),
] 


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT ) 
