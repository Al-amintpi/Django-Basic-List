from rest_framework.parsers import JSONParser,ParseError
from django.shortcuts import render
from rest_framework import viewsets
from crudapp.models import *
from .serializers import PersonSerializers


class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializers
