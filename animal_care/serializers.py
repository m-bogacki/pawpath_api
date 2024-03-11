from rest_framework import serializers

from animals.models import Animal
from .models import AnimalCare, Offer
from account.serializers import UserListSerializer
from animals.serializers import AnimalListSerializer
     
     
     
class OfferSerializer(serializers.ModelSerializer):
    carrer = UserListSerializer(many=False, read_only=True)
    viewed = serializers.BooleanField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Offer
        exclude = ["animal_care"]
     

class AnimalCareListSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    animals = AnimalListSerializer(many=True, read_only=True)
    
    class Meta:
        model = AnimalCare
        fields = "__all__"
        
class AnimalCareCreateSerializer(serializers.ModelSerializer):
    animals = serializers.PrimaryKeyRelatedField(many=True, queryset=Animal.objects.all())
    
    class Meta:
        model = AnimalCare
        exclude = ["carrer", "status"]
        