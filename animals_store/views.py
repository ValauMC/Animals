from rest_framework import viewsets
from .models import Species, Animals, Behavior
from .serializer import SpeciesSerializer, AnimalsSerializer, BehaviorSerializer

# Create your views here.
class SpeciesViewSet(viewsets.ModelViewSet):
    serializer_class = SpeciesSerializer
    queryset = Species.objects.all()

class AnimalsViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()

class BehaviorViewSet(viewsets.ModelViewSet):
    serializer_class = BehaviorSerializer
    queryset = Behavior.objects.all()