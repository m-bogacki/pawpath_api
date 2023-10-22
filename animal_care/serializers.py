from rest_framework import serializers
from .models import AnimalCare
from account.serializers import UserListSerializer
from animals.serializers import AnimalListSerializer


class AnimalCareCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnimalCare
        fields = "__all__"
        
        
class AnimalCareListSerializer(serializers.ModelSerializer):
    carrer = UserListSerializer(many=False)
    animal = AnimalListSerializer(many=False)
    
    
    class Meta:
        model = AnimalCare
        fields = "__all__"