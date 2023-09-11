from django.shortcuts import render
from rest_framework import generics
from scenario_collection.models import ScenarioCollection
from .serializers import ScenarioCollectionSerializer

class ScenarioCollectionListCreateView(generics.ListCreateAPIView):
    queryset = ScenarioCollection.objects.all()
    serializer_class = ScenarioCollectionSerializer

class ScenarioCollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScenarioCollection.objects.all()
    serializer_class = ScenarioCollectionSerializer
