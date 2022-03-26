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
    ProjectName= models.CharField(max_length=100,verbose_name = "Project Name")
    ProjectDescription= models.TextField(blank=True, null= True ,verbose_name = "Description")
    Projectdate=models.DateField(blank=True,verbose_name = "Date")
    ProjectPOCname=models.CharField(max_length=100,verbose_name = "Contact person")
    ProjectPOCnum=models.CharField(max_length=10 ,verbose_name = "Contact number")
    Projectype= models.TextField(
        choices = Type_Choices,verbose_name = "Type")
    Projectlink = models.URLField(help_text="url link",blank=True)
    ProjectTechnicalspecification = models.FileField(upload_to ='doc/',verbose_name="Technical specification",blank=True,help_text= 'The file must be in pdf')
    ProjectWhitepapers = models.FileField(upload_to ='doc/whitepapers',verbose_name='White papers',blank=True,help_text= 'The file must be in pdf')
    ProjectCoverphoto = models.ImageField(upload_to='images/coverphoto/ProjectDetails/', height_field=None, width_field=None, max_length=100,default='defaultcover.jpg', help_text= 'The size must be --- and the resoultion is ---')
    Projectpicture =models.ImageField(upload_to='images/Photo/ProjectDetails/', height_field=None, width_field=None, max_length=100,default='default.jpg',help_text= 'The size must be --- and the resoultion is ---')
    
    
    def __str__(self):
        return self.ProjectName 

