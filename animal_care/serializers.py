from rest_framework.serializers import ModelSerializer
from .models import AnimalCare


class AnimalCareSerializer(ModelSerializer):
    class Meta:
        model = AnimalCare