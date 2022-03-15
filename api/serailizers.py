
# import serializer from rest_framework
from rest_framework import serializers
from .models import EventDetails, ProgramDetails, ProjectDetails, ServiceDetails



class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDetails
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetails
        fields = '__all__'
   
