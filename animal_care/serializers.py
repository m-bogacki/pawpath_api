from rest_framework import serializers
from .models import AnimalCare, Offer
from account.serializers import UserListSerializer
from animals.serializers import AnimalListSerializer
     
class OfferSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    carrer = UserListSerializer(many=False, read_only=True)
    
    class Meta:
        model = Offer
        exclude = ["animal_care"]
     
class AnimalCareSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    animal = AnimalListSerializer(many=False, read_only=True)
    
    class Meta:
        model = AnimalCare
        exclude = ["carrer"]
        