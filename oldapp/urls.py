from django.conf.urls import patterns, url
from oldapp import views

urlpatterns = patterns('',
	                   url(r'^$', views.home, name='oldhome'),
	                   url(r'^credit/$', views.credit_card, name='credit_form'),
	                   url(r'^client_token/$', views.client_token, name='client_token'),
	                   url(r'^purchase/$', views.purchase, name='purchase'),)
