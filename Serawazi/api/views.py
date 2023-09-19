from .serializers import BadgesSerializer, ScenarioCollectionSerializer
from rest_framework.views import APIView
from scenario_collection.models import ScenarioCollection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Category
from .serializers import CategorySerializer
from .models import VirtualItem
from .serializers import VirtualItemSerializer
# from .models import Badges, Tutorial
from .serializers import BadgesSerializer, TutorialSerializer
from tutorials.models import Tutorial
from badges.models import Badges





class BadgesList(APIView):
    def get(self, request):
        badges = Badges.objects.all()
        serializer = BadgesSerializer(badges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BadgesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BadgesDetail(APIView):
    def get(self, request, id):
        try:
            badge = Badges.objects.get(id=id)
            serializer = BadgesSerializer(badge)
            return Response(serializer.data)
        except Badges.DoesNotExist:
            return Response({"detail": "Badge not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            badge = Badges.objects.get(id=id)
            serializer = BadgesSerializer(badge, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Badges.DoesNotExist:
            return Response({"detail": "Badge not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            badge = Badges.objects.get(id=id)
            badge.delete()
            return Response({"detail": "Badge deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Badges.DoesNotExist:
            return Response({"detail": "Badge not found"}, status=status.HTTP_404_NOT_FOUND)


# Tutorial API views
class TutorialList(APIView):
    def get(self, request):
        tutorials = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorialDetail(APIView):
    def get(self, request, id):
        try:
            tutorial = Tutorial.objects.get(id=id)
            serializer = TutorialSerializer(tutorial)
            return Response(serializer.data)
        except Tutorial.DoesNotExist:
            return Response({"detail": "Tutorial not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            tutorial = Tutorial.objects.get(id=id)
            serializer = TutorialSerializer(tutorial, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tutorial.DoesNotExist:
            return Response({"detail": "Tutorial not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            tutorial = Tutorial.objects.get(id=id)
            tutorial.delete()
            return Response({"detail": "Tutorial deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Tutorial.DoesNotExist:
            return Response({"detail": "Tutorial not found"}, status=status.HTTP_404_NOT_FOUND)


class ScenarioCollectionListView (APIView):
   def get(self, request):
    message = ScenarioCollection.objects.all()
    serializer = ScenarioCollectionSerializer(message, many =True)
    return Response(serializer.data)
   def post(self,request):
        serializer = ScenarioCollectionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
class ScenarionCollectionDetailView(APIView):
    def get(self, request,id,format = None):
        try:
            message= ScenarioCollection.objects.get(id=id)
            serializer = ScenarioCollectionSerializer(message)
            return Response(serializer.data)
        except ScenarioCollection.DoesNotExist:
            raise NotFound("Messge not found")
    def put(self, request,id,format = None):
       message = ScenarioCollection.objects.get(id=id)
       serializer = ScenarioCollectionSerializer(message,request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id,format = None):
        message=ScenarioCollection.objects.get(id=id)
        message.delete()
        return Response("Message has been Deleted", status = status.HTTP_204_NO_CONTENT)
    

#category model

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response("Category has been successfully deleted", status=status.HTTP_404_NOT_FOUND)
        


#Virtual items

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
    



