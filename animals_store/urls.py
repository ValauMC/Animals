from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'species', SpeciesViewSet)
router.register(r'animals', AnimalsViewSet)
router.register(r'behaviors', BehaviorViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]