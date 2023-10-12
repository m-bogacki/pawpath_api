from rest_framework import serializers
from .models import Animal, CareInstructions
from account.models import User
from account.serializers import UserSerializer


class CareInstructionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CareInstructions
        fields = "__all__"



class AnimalListSerializer(serializers.ModelSerializer):
    care_instructions = CareInstructionsSerializer()
    owner = UserSerializer()

    class Meta:
        model = Animal
        fields = "__all__"
        

class AnimalCreateSerializer(serializers.ModelSerializer):
    care_instructions = CareInstructionsSerializer()
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Animal
        fields = "__all__"
        
    def create(self, validated_data):
        owner = validated_data.pop('owner')
        care_instructions = validated_data.pop('care_instructions')
        cr = CareInstructions.objects.create(**care_instructions)
        animal = Animal.objects.create(owner=owner, care_instructions=cr, **validated_data)
        return animal