from rest_framework import serializers
from .models import VirtualItem

class VirtualItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualItem
        fields = '__all__'
