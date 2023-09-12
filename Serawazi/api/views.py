from rest_framework import generics, status
from rest_framework.response import Response
from scenario_collection.models import ScenarioCollection
from .serializers import ScenarioCollectionSerializer

class ScenarioCollectionListCreateView(generics.ListCreateAPIView):
    queryset = ScenarioCollection.objects.all()
    serializer_class = ScenarioCollectionSerializer

    def create(self, request, *args, **kwargs):
        return self.create_scenario(request)

    def create_scenario(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        return self.list_scenarios(request)

    def list_scenarios(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ScenarioCollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScenarioCollection.objects.all()
    serializer_class = ScenarioCollectionSerializer

    def update(self, request, *args, **kwargs):
        return self.update_scenario(request, *args, **kwargs)

    def update_scenario(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return self.retrieve_scenario(request, *args, **kwargs)

    def retrieve_scenario(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return self.destroy_scenario(request, *args, **kwargs)

    def destroy_scenario(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
