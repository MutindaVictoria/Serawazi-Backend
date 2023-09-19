
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
from User_Registration.models import CustomUser,Admins,Gamer
from Scenarios.models import Scenarios
from scenario_collection.models import ScenarioCollection
from .models import Category
from .models import VirtualItem


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  
        user.save()
        return user


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ['username', 'email', 'password']        

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ('user','email','password')





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = "__all__"
from rest_framework import serializers
from scenario_collection.models import ScenarioCollection
from .models import Category
from .models import VirtualItem



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


