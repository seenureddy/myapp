from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from .models import Snippet
from .serializers import UserSerializer, GroupSerializer, SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializers_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    qureyset = Group.objects.all()
    serializers_class = GroupSerializer

class JSONResponse(HttpResponse):
    """
    HttpResponse that render it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs)
    
class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all the code snippet or create new snippet.
    """
    qureyset = Snippet.objects.all()
    serializers_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
    generics.GenericAPIView):
    """ 
    Retrieve, update or delete a code snippet.
    """

    qureyset = Snippet.objects.all()
    serializers_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)