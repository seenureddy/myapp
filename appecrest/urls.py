from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = patterns(
    'appecrest.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_details'),
    )

urlpatterns = format_suffix_patterns(urlpatterns)