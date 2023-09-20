
# from rest_framework import serializers

# from User_Registration.models import Admin, RegularUser,CustomUser


# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = ('id', 'first_name', 'last_name', 'email', 'age', 'gender', 'achievements')

# class RegularUserSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = RegularUser
#         fields = ['id', 'first_name', 'last_name', 'email', 'confirm_password']  

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         confirm_password = validated_data.pop('confirm_password', None)
        
#         # Create a new CustomUser instance
#         custom_user = CustomUser(**validated_data)
#         if password:
from rest_framework import serializers
from User_Registrations.models import CustomUser 
from Scenarios.models import Scenarios
from scenario_collection.models import ScenarioCollection
from .models import Category
from .models import VirtualItem

from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ObjectDoesNotExist


from rest_framework import serializers
from User_Registrations.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError('Invalid credentials')
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')
        
        data['user'] = user
        return data

    
class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = "__all__"

class ScenarioCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ScenarioCollection
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        


class VirtualItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualItem
        fields = '__all__'