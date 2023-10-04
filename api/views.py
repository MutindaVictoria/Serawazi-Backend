from .serializers import ScenarioCollectionSerializer
from rest_framework.views import APIView
from scenario_collection.models import ScenarioCollection
from rest_framework.response import Response
from rest_framework import status
from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken .models import Token
from User_Registrations.models import CustomUser
from django.contrib .auth .models import User

from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from .models import Category
from .serializers import CategorySerializer
from .models import VirtualItem
from .serializers import VirtualItemSerializer
from .models import Scenarios
from .models import Badges


from django.urls import path
from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# from api.roles import roles
from User_Registrations.models import CustomUser
from django.contrib.auth.models import User
from .serializers import LoginSerializer, UserSerializer, ScenariosSerializer, ScenarioCollectionSerializer, CategorySerializer, VirtualItemSerializer
from Scenarios.models import Scenarios
from scenario_collection.models import ScenarioCollection
from .models import Category, VirtualItem
from rest_framework.exceptions import ValidationError, NotFound
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required
from api.roles  import ROLES_PERMISSIONS_MAPPING
# from User_Registration import ROLES_PERMISSIONS_MAPPING

# from User_Registration import Role
from django.contrib.auth import get_user_model


# # User = get_user_model()



# # class UserRegistrationView(APIView):
# #     def post(self, request):
# #         data = request.data
# #         serializer = UserSerializer(data=data)

# #         if serializer.is_valid():
# #             user = serializer.save()

# #             gamer_role, _ = Role.objects.get_or_create(name="Gamer")
# #             user.roles.add(gamer_role)

# #             return Response(serializer.data, status=status.HTTP_201_CREATED)

# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# # # @permission_classes([IsAuthenticated])
# # class UserRegistrationListView(generics.ListAPIView):
# #     queryset = CustomUser.objects.all()
# #     serializer_class = UserSerializer


# # @permission_classes([IsAuthenticated])    
# # class UserRegistrationUpdateView(generics.UpdateAPIView):
# #     queryset = CustomUser.objects.all()
# #     serializer_class = UserSerializer
# #     lookup_field = 'id' 




# # class UserRegistrationDeleteView(generics.DestroyAPIView):
# #     queryset = CustomUser.objects.all()
# #     serializer_class = UserSerializer

# #     def perform_destroy(self, instance):
# #         instance.delete()

# #     def delete(self, request, *args, **kwargs):
# #         instance = self.get_object()
# #         self.perform_destroy(instance)
# #         return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# # class UserLoginView(APIView):
# #     def post(self, request):
# #         serializer = LoginSerializer(data=request.data)
# #         if serializer.is_valid():
# #             user = serializer.validated_data['user']
# #             token, _ = Token.objects.get_or_create(user=user)
# #             return Response({'token': token.key}, status=status.HTTP_200_OK)
# #         return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)




from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from User_Registrations.models import CustomUser,Roles
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Category
from .serializers import CategorySerializer
from .models import VirtualItem
from .import roles
from .serializers import VirtualItemSerializer
from rest_framework import generics
from api.roles import ROLES_PERMISSIONS_MAPPING


from . import models


User = get_user_model()

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            
            # Assuming "Gamer" role exists in your ROLES_PERMISSIONS_MAPPING
            gamer_permissions = ROLES_PERMISSIONS_MAPPING.get("Gamer", [])
            
            
            (user, gamer_permissions)

            response_data = {
                "message": "Registration successful. You have been logged in."
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRegistrationUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id' 

class UserRegistrationDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class UserLoginView(APIView):
    def post(self, request):
        username =request.data.get('username')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({'Invalid Credentials'},status= status.HTTP_401_UNAUTHORIZED)
        if user.check_password (password):
            login (request,user)
            return Response({'Login succesfull'},status=status.HTTP_200_OK)
        else:
            return Response({'Invalid Credentials'},status= status.HTTP_401_UNAUTHORIZED)

        # serializer = LoginSerializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.validated_data['user']
        #     token, _ = Token.objects.get_or_create(user=user)
        #     return Response({'token': token.key}, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)




class ScenariosListView(APIView):
    def get(self, request):
        scenarios = Scenarios.objects.all()
        serializer = ScenariosSerializer(scenarios, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ScenariosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        scenarios = self.get_object(id)
        serializer = ScenariosSerializer(scenarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ScenariosDetailView(APIView):
    def get(self, request,id,format = None):
        scenarios= Scenarios.objects.get(id=id)
        serializer = ScenariosSerializer(scenarios)
        return Response(serializer.data)
    

    def put(self, request,id,format = None):
       scenarios = Scenarios.objects.get(id=id)
       serializer = ScenariosSerializer(scenarios,request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       
       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id,format = None):
        scenarios = Scenarios.objects.get(id=id)
        scenarios.delete()
        return Response("scenariosDeleted", status = status.HTTP_204_NO_CONTENT)
    
           






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
