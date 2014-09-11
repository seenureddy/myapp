from django.conf.urls import patterns, url
from newapp import views
urlpatterns = patterns('',
	                   url(r'^$', views.home, name='home'),
	                   )