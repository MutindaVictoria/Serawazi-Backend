
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import login,authenticate
# from User_Registration.models import Admin, RegularUser
# from .serializers import AdminSerializer, RegularUserSerializer
# from django.db import IntegrityError
# from rest_framework.permissions import AllowAny
# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView


from django.urls import path
from django.contrib.auth import login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from User_Registration.models import CustomUser, Admins, Gamer  
from .serializers import CustomUserSerializer, AdminsSerializer, GamerSerializer  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from Scenarios.models import Scenarios
from .serializers import ScenariosSerializer




class CustomUserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()  
        serializer = CustomUserSerializer(users, many=True)  
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserDetailView(APIView):
    def get(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)

class AdminsRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        if Admins.objects.filter(user=username).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_409_CONFLICT)

        admins = Admins.objects.create(user=username)
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    


class AdminsLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')


        try:
            admins = Admins.objects.get(user=username)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        except Admins.DoesNotExist:
            return Response({'message': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)




class GamerRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, email=email, password=password)

        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    
class GamerLoginView(APIView):
    def post(self, request):
        user = request.data.get('user')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            supplier = Gamer.objects.get(user=user, email=email)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        except Gamer.DoesNotExist:
            return Response({'message': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)
        

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
    
           






    



















