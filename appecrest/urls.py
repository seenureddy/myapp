from django.conf.urls import url, patterns

from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from appecrest.views import UserViewSet, SnippetViewSet, api_root

snippet_list = SnippetViewSet.as_view({
	'get': 'list',
	'post': 'create'
	})

snippet_details = SnippetViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
	})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight',
    }, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
	'get': 'list'
	})

user_details = UserViewSet.as_view({
	'get': 'retrieve'
	})

urlpatterns = patterns(
    '',
    url(r'^api-root/', api_root),
    url(r'^users/', user_list, name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_details, name='users-details'),
    url(r'^snippets/$', snippet_list, name='snippets-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_details, name='snippets-details'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippets-highlight'),
    )

urlpatterns = format_suffix_patterns(urlpatterns)