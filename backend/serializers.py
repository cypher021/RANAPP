from rest_framework import serializers
from .models import ProjectDetails , EventDetails , ServiceDetails , ProgramDetails



class Projectserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProjectDetails
        fields = '__all__'


class Eventserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EventDetails
        fields = '__all__'


class Serviceserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ServiceDetails
        fields = '__all__'



class Programserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramDetails
        fields = '__all__'
