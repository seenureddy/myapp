from django.conf.urls import patterns, include, url
from rest_framework import routers

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from appecrest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users-set')
router.register(r'groups', views.GroupViewSet, base_name='groups-set')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='mainhome'),
    # url(r'^myapp/', include('myapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^newapp/', include('newapp.urls')),
    url(r'^oldapp/', include('oldapp.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'$', 'rackdjango.views.home', name='home'),
    url(r'^profile/$', 'rackdjango.views.profile', name='profile'),
    
    url(r'^', include(router.urls)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),

)
