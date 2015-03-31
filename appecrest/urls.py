from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from appecrest import views

urlpatterns = patterns(
    '',
    url(r'^api-root/', views.api_root),
    url(r'^users/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetails.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
    )

urlpatterns = format_suffix_patterns(urlpatterns)