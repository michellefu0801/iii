"""finalproject URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from views import welcome, index, login, register, homepage, skills, index, map, skills_recommend
from jobs.views import JobList, TaiwanMap_test2, job_recommend
from django.contrib.auth.views import  logout
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^welcome/$',welcome),
	url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
	url(r'^accounts/register/$',register),
	url(r'^JobList/$',JobList),
	url(r'^TaiwanMap_test2/$',TaiwanMap_test2),
	url(r'^homepage/$',homepage),
	url(r'^homepage/homepage',homepage),
	url(r'^homepage/login/',login),
	url(r'^homepage/skills',skills),
	url(r'^homepage/job_recommend',job_recommend),
	url(r'^homepage/map',map),
	url(r'^homepage/homepage.html%20',homepage),
	url(r'^skills/$', skills),
	url(r'^skills/skills', skills),
	url(r'^skills/job_recommend', job_recommend),
	url(r'^skills/skills_recommend', skills_recommend),
	url(r'^skills/homepage', homepage),
	url(r'^skills/map', map),
	url(r'^map/$', map),
	url(r'^map/map', map),
	url(r'^map/job_recommend',job_recommend),
	url(r'^map/skills_recommend',skills_recommend),
	url(r'^job_recommend/$', job_recommend),
	url(r'^skills_recommend/$', skills_recommend),
	url(r'^skills_recommend/job_recommend', job_recommend),
	url(r'^skills_recommend/map', map),
	url(r'^skills_recommend/skills_recommend', skills_recommend),
] 

