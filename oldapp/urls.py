from django.conf.urls import patterns, url
from oldapp import views

urlpatterns = patterns('',
	                   url(r'^$', views.home, name='oldhome'),
	                   url(r'^credit/$', views.credit_card, name='credit_form'),)
