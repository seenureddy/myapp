from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group

from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, detail_route
from rest_framework import status, viewsets, permissions, renderers

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, GroupSerializer, SnippetSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializers_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializers_class = GroupSerializer

class JSONResponse(HttpResponse):
    """
    HttpResponse that render it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs)
    
class SnippetViewSet(viewsets.ModelViewSet):
    """
    List all the code snippet or create new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(("GET", ))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippet': reverse('snippet-list', request=request, format=format)
        })
