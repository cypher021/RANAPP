from django.contrib import admin
from .models import ProgramDetails, EventDetails , ProjectDetails , ServiceDetails
# Register your models here.
admin.site.register(ProgramDetails)
admin.site.register(EventDetails)
admin.site.register(ProjectDetails)
admin.site.register(ServiceDetails)

