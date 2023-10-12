from django.shortcuts import render
from rest_framework import generics
from .models import AnimalCare
from .serializers import AnimalCareSerializer
from rest_framework.response import Response

# Create your views here.

class AnimalCareListCreateView(generics.ListCreateAPIView):
    queryset = AnimalCare.objects.all()
    
    def list(self, request):
        self.queryset = self.queryset.filter()
        serializer = AnimalCareSerializer(self.queryset, many=True)
        return Response(serializer.data)