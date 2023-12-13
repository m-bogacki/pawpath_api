from rest_framework import serializers
from .models import Animal, CareInstructions
from account.models import User
from account.serializers import UserListSerializer


class CareInstructionsSerializer(serializers.ModelSerializer):
    animal_id = serializers.IntegerField(source="animal.id", read_only=True)
    animal_name = serializers.CharField(source="animal.name", read_only=True)
    
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
    size = serializers.CharField(read_only = True)
    care_instructions = CareInstructionsSerializer(read_only=True)
    
    class Meta:
        model = Animal
        fields = "__all__"
    
    