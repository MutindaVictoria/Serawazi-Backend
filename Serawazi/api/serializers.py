from rest_framework import serializers
from scenario_collection.models import ScenarioCollection

class ScenarioCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ScenarioCollection
        fields='__all__'