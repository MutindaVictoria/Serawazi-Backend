from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VirtualItem
from .serializers import VirtualItemSerializer

class VirtualItemDetail(APIView):
    def get(self, request):
        virtual_items = VirtualItem.objects.all()
        serializer = VirtualItemSerializer(virtual_items, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = VirtualItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VirtualItemUpdate(APIView):
    def get(self, request, id):
        try:
            virtual_item = VirtualItem.objects.get(id=id)
            serializer = VirtualItemSerializer(virtual_item)
            return Response(serializer.data)
        except VirtualItem.DoesNotExist:
            return Response({"detail": "VirtualItem not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            virtual_item = VirtualItem.objects.get(id=id)
            serializer = VirtualItemSerializer(virtual_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except VirtualItem.DoesNotExist:
            return Response({"detail": "VirtualItem not found"}, status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, id):
        try:
            virtual_item = VirtualItem.objects.get(id=id)
            virtual_item.delete()
            return Response({"detail": "VirtualItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except VirtualItem.DoesNotExist:
            return Response({"detail": "VirtualItem not found"}, status=status.HTTP_404_NOT_FOUND)
    
