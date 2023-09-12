from rest_framework import serializers
# from ser_registration.se import User_Registration
from User_Registration.models import User_Registration
from Scenarios.models import Scenarios



class User_RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration
        fields = "__all__"

class User_RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration
        fields = "__all__"



class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = "__all__"

class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = "__all__"