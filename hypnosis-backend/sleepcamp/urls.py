"""teenkerOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from .views import RegisterView

urlpatterns =  patterns('',
    url(r'^register', RegisterView.as_view()),
)

__author__ = "moonmoonbird"
__copyright__ = "Copyright 2015 , The TeenkerOperations Project"
__version__ = "1.0.1"
__maintainer__ = "moonmoonbird"
__email__ = "lomoonmoonbird@gmail.com"
__status__ = "Development"
