from rest_framework import viewsets

# from backend.forms import membershipform

from .serializers import Categoryserializer, Eventserializer, Memberserializer, Programserializer, Projectserializer, Serviceserializer, Tenureserializer
from.models import Categorymember, ServiceDetail , ProjectDetail ,ProgramDetail ,EventDetail, TenureDetail, membership

# Create your views here.

#for services
class ServicesViews(viewsets.ModelViewSet):
    queryset = ServiceDetail.objects.all() 
    serializer_class = Serviceserializer

# For Projects Titles
class ProjectsViews(viewsets.ModelViewSet):
    queryset = ProjectDetail.objects.all() 
    serializer_class = Projectserializer

# For Programs Titles
class ProgramsViews(viewsets.ModelViewSet):
    queryset = ProgramDetail.objects.all() 
    serializer_class = Programserializer

# For Events Titles
class EventsViews(viewsets.ModelViewSet):
    queryset = EventDetail.objects.all() 
    serializer_class = Eventserializer

class TenureViews(viewsets.ModelViewSet):
    queryset = TenureDetail.objects.all() 
    serializer_class = Tenureserializer
    
class CategoryViews(viewsets.ModelViewSet):
    queryset = Categorymember.objects.all() 
    serializer_class = Categoryserializer

class MembershipViews(viewsets.ModelViewSet):
    queryset = membership.objects.all() 
    serializer_class = Memberserializer


    