from django.conf.urls import url, patterns

urlpatterns = patterns(
    'appecrest.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/?(P<pk>[0-9]+)/$', 'snippet_details'),
    )