from rest_framework import generics
from .models import VirtualItem
from .serializers import VirtualItemSerializer

class VirtualItemListCreateView(generics.ListCreateAPIView):
    queryset = VirtualItem.objects.all()
    serializer_class = VirtualItemSerializer

class VirtualItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VirtualItem.objects.all()
    serializer_class = VirtualItemSerializer
