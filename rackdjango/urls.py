from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from appecrest import views


router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, base_name='snippets')
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'groups', views.GroupViewSet, base_name='groups')


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newapp/', include('newapp.urls')),
    url(r'^oldapp/', include('oldapp.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^$', 'rackdjango.views.home', name='home'),
    url(r'^profile/$', 'rackdjango.views.profile', name='profile'),
    
    url(r'^restapi/', include('appecrest.urls')),
    url(r'^sets/', include(router.urls)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),

)
