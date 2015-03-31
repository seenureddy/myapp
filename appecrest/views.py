from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group

from rest_framework import status
from rest_framework import viewsets
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
    
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all the code snippet or create new snippet.
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTPRESPONSE_201_CREATED)
        return Response(serializer.error, status=status.HTTPRESPONSE_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_details(request, pk, format=None):
    """ 
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.filter(pk=pk)
    except Snippet.DoesNotExist:
        raise HttpResponse(status=status.HTTPRESPONSE_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.error, status=status.HTTPRESPONSE_400_BAD_REQUEST)
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=HttpResponse_204_NO_CONTENT)