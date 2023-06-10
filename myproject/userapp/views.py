from django.shortcuts import render
from .models import UserData
from .serializer import Dataserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


class StudentModelViewset(viewsets.ModelViewSet):
   queryset = UserData.objects.all()
   serializer_class = Dataserializer
   authentication_classes = [SessionAuthentication]
   #permission_classes = [IsAuthenticated]
   permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

