from django.shortcuts import render
from django.http import JsonResponse
from .serailizers import EventSerializer, ProgramSerializer, ProjectSerializer, ServicesSerializer
from .models import EventDetails, ProgramDetails, ProjectDetails, ServiceDetails 
from rest_framework import viewsets
from rest_framework.decorators import api_view
# Create your views here.


# @api_view(['GET', 'POST', 'DELETE'])
class ProgramViewsets(viewsets.ModelViewSet):
    queryset = ProgramDetails.objects.all()
    serializer_class = ProgramSerializer

# @api_view(['GET', 'POST', 'DELETE'])
class EventViewsets(viewsets.ModelViewSet):
    queryset = EventDetails.objects.all()
    serializer_class = EventSerializer

# @api_view(['GET', 'POST', 'DELETE'])
class ServiceViewsets(viewsets.ModelViewSet):
    queryset = ServiceDetails.objects.all()
    serializer_class = ServicesSerializer

# @api_view(['GET', 'POST', 'DELETE'])
class ProjectViewsets(viewsets.ModelViewSet):
    queryset = ProjectDetails.objects.all()
    serializer_class = ProjectSerializer



