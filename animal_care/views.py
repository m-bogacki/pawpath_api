from django.shortcuts import render
from rest_framework import generics
from .models import AnimalCare
from .serializers import AnimalCareSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
# Create your views here.

class AnimalCareListView(generics.ListAPIView):
    queryset = AnimalCare.objects.all()
    serializer_class = AnimalCareSerializer

                
class AnimalCareCreateView(generics.CreateAPIView):
    queryset = AnimalCare.objects.all()
    serializer_class = AnimalCareSerializer


