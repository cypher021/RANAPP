from django.db import models
Type_Choices=(
    ('Online','Online'),
    ('Physical','Physical')
)
# Create your models here.
class ProgramDetails(models.Model):
    ProgramName= models.CharField(max_length=100)
    Description= models.TextField(blank=False)
    Objectives= models.TextField(blank=False , help_text='Enter in bullet points')
    Goals= models.TextField(blank=False,help_text='Enter in bullet points')
    StartDate= models.DateField(blank=False)
    EndDate= models.DateField(blank=False)
    ProgramType = models.TextField( 
        choices = Type_Choices)

    def __str__(self):
        return self.ProgramName


class EventDetails(models.Model):
    EventName= models.CharField(max_length=100)
    EventDescription= models.TextField(blank=False)
    Eventdate=models.DateField(blank=False)
    eventype= models.TextField(
        choices = Type_Choices)


    def __str__(self):
        return self.EventName

class ServiceDetails(models.Model):
    ServiceName= models.CharField(max_length=100)
    ServiceDescription= models.TextField(blank=False)
    Servicedate=models.DateField(blank=False)
    servicetype= models.TextField(
        choices = Type_Choices)



    def __str__(self):
        return self.ServiceName

class ProjectDetails(models.Model):
    ProjectName= models.CharField(max_length=100)
    ProjectDescription= models.TextField(blank=False)
    Projectdate=models.DateField(blank=False)
    Projectype= models.TextField(
        choices = Type_Choices)


    def __str__(self):
        return self.ProjectName


