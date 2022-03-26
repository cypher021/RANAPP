from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from .views import *
from django.conf.urls.static import static





route = routers.DefaultRouter()
route.register('Services', ServicesViews)
route.register('Projects', ProgramsViews)
route.register('Programs', ProjectsViews)
route.register('Events', EventsViews)



urlpatterns = [
    path('', include(route.urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)