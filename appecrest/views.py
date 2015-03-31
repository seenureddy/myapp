from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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
    
@csrf_exempt
def snippet_list(request):
    """
    List all the code snippet or create new snippet.
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.error, status=400)

@csrf_exempt
def snippet_details(request, pk):
    """ 
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.filter(pk=pk)
    except Snippet.DoesNotExist:
        raise HttpResponse(status=404)
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.error, status=400)
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)