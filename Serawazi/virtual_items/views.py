from rest_framework.response import Response
from django.views import View
from .models import VirtualItem
from rest_framework import status

from .serializers import VirtualItemSerializer

class VirtualItemDetail(View):
    def get(self, request, id):
        virtual_item = VirtualItem.objects.get(id=id)
        serializer = VirtualItemSerializer(virtual_item)
        return Response(serializer.data)

class VirtualItemList(View):
    def get(self, request):
        virtual_items = VirtualItem.objects.all()
        serializer = VirtualItemSerializer(virtual_items, many=True)
        return Response(serializer.data)


class VirtualItemCreate(View):
    def post(self, request):
        item_data = request.data
        serializer = VirtualItemSerializer(data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VirtualItemUpdate(View):
    def put(self, request, id):
        virtual_item = VirtualItem.objects.get(id=id)
        serializer = VirtualItemSerializer(virtual_item, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VirtualItemDelete(View):
    def delete(self, request, id):
        virtual_item = VirtualItem.objects.get(id=id)
        virtual_item.delete()
        return Response({ 'VirtualItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
