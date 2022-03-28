from django.contrib import admin
from .models import ProgramDetail, EventDetail , ProjectDetail , ServiceDetail
# Register your models here.
admin.site.register(ProgramDetail)
admin.site.register(EventDetail)
admin.site.register(ProjectDetail)
admin.site.register(ServiceDetail)

