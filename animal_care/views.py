from django.shortcuts import render
from rest_framework import generics
from .models import AnimalCare
from .serializers import AnimalCareCreateSerializer, AnimalCareListSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AnimalCareListView(generics.ListAPIView):
    queryset = AnimalCare.objects.all()
    
    def list(self, request):
        self.queryset = self.queryset.filter()
        serializer = AnimalCareListSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

            
class AnimalCareCreateView(generics.CreateAPIView):
    queryset = AnimalCare.objects.all()
    
    def create(self,request, *args, **kwargs):
        serializer = AnimalCareCreateSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.data)