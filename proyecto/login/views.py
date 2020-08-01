from django.shortcuts import render
from rest_framework import viewsets
from .models import Login
from .serializers import LoginSerializer

class LoginViewset(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Login.objects.all()
