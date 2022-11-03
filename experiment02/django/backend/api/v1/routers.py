from rest_framework import routers
from .viewsets import ProfileViewSet, ErrorViewset, TimeoutViewset

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet , basename='profile')
router.register(r'error', ErrorViewset , basename='error')
router.register(r'timeout', TimeoutViewset , basename='timeout')