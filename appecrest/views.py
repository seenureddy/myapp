from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer


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