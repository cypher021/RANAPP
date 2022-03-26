from rest_framework import viewsets

from .serializers import Eventserializer, Programserializer, Projectserializer, Serviceserializer
from.models import ServiceDetails , ProjectDetails ,ProgramDetails ,EventDetails

# Create your views here.

#for services
class ServicesViews(viewsets.ModelViewSet):
    queryset = ServiceDetails.objects.all() 
    serializer_class = Serviceserializer

# For Projects Titles
class ProjectsViews(viewsets.ModelViewSet):
    queryset = ProjectDetails.objects.all() 
    serializer_class = Projectserializer

# For Programs Titles
class ProgramsViews(viewsets.ModelViewSet):
    queryset = ProgramDetails.objects.all() 
    serializer_class = Programserializer

# For Events Titles
class EventsViews(viewsets.ModelViewSet):
    queryset = EventDetails.objects.all() 
    serializer_class = Eventserializer