from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Users
from .serializers import UsersSerializer
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
