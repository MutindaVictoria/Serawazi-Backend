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


