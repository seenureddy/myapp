from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
    url(r'$', 'myapp.views.home', name='home'),
    url(r'^profile/$', 'myapp.views.profile', name='profile'),


)
