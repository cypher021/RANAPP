from .views import  ProgramViewsets ,EventViewsets, ProjectViewsets, ServiceViewsets
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'Program',ProgramViewsets , basename='Program')
router.register(r'Events',EventViewsets , basename='Events')
router.register(r'Services',ServiceViewsets , basename='Services')
router.register(r'Projects',ProjectViewsets , basename='Projects')



urlpatterns = router.urls