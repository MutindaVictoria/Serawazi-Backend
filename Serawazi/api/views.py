from rest_framework import generics, status
from rest_framework.response import Response
from scenario_collection.models import ScenarioCollection
from .serializers import ScenarioCollectionSerializer

class ScenarioCollectionListCreateView(generics.ListCreateAPIView):
    queryset = ScenarioCollection.objects.all()
    serializer_class = ScenarioCollectionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScenarioCollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScenarioCollection.objects.all()
    serializer_class = ScenarioCollectionSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
