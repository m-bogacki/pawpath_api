from rest_framework import serializers
from .models import Animal, CareInstructions
from account.models import User
from account.serializers import UserListSerializer


class CareInstructionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CareInstructions
        fields = "__all__"



class AnimalListSerializer(serializers.ModelSerializer):
    care_instructions = CareInstructionsSerializer()
    owner = UserListSerializer(many=False)

    class Meta:
        model = Animal
        fields = "__all__"
        

class AnimalCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Animal
        fields = "__all__"
        
    def create(self, validated_data):
        animal = Animal.objects.create(**validated_data)
        return animal