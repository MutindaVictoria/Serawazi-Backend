# from django.shortcuts import render

# Create your views here.
from .serializers import User_RegistrationSerializer
from .serializers import ScenariosSerializer
from rest_framework.views import APIView
from User_Registration.models import User_Registration
from Scenarios.models import Scenarios
from rest_framework.response import Response
from rest_framework import status



class User_RegistrationListView (APIView):
   def get(self, request):
    user_registration = User_Registration.objects.all()
    serializer = User_RegistrationSerializer(user_registration, many =True)
    return Response(serializer.data)
   def post(self,request):
        serializer = User_RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
   

class User_RegistrationDetailView(APIView):
    def get(self, request,id,format = None):
        user_registration= User_Registration.objects.get(id=id)
        serializer = User_RegistrationSerializer(user_registration)
        return Response(serializer.data)
    def put(self, request,id,format = None):
       user_registration = User_Registration.objects.get(id=id)
       serializer = User_RegistrationSerializer(user_registration,request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id,format = None):
        user_registration=User_Registration.objects.get(id=id)
        user_registration.delete()
        return Response("user_registrationDeleted", status = status.HTTP_204_NO_CONTENT)
        
class ScenariosListView (APIView):
   def get(self, request):
    scenarios = Scenarios.objects.all()
    serializer = ScenariosSerializer(scenarios, many =True)
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
        serializer = User_RegistrationSerializer(scenarios)
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








