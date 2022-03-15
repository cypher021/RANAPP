from django.contrib import admin
from .models import  EventDetails, ProgramDetails, ProjectDetails, ServiceDetails

admin.site.register(EventDetails)
admin.site.register(ProgramDetails)
admin.site.register(ServiceDetails)
admin.site.register(ProjectDetails)