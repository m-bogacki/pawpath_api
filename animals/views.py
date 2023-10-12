from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Animal
from .serializers import AnimalListSerializer, AnimalCreateSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class AnimalListCreate(generics.ListCreateAPIView):
    queryset = Animal.objects.all()

    def list(self, request):
        self.queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        if id_filter:
            self.queryset = self.queryset.filter(id=id_filter)
        serializer = AnimalListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AnimalCreateSerializer(data=request.data)
        try:
            if not request.user.is_authenticated:
                raise AuthenticationFailed("User is not authenticated", 403)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data=serializer.data)      
        except ValidationError as e:
            return Response(data={"error": str(e.detail)})

class AnimalRetrieve(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    
    def retrieve(self, request, id):
        self.queryset = self.queryset.all()
        try:
            if id:
                self.queryset = self.queryset.get(id=id)
                
            serializer = AnimalListSerializer(self.queryset)
            return Response(serializer.data)
        
        except ObjectDoesNotExist as e:
            return Response(data={"error": "There is no Animal with this ID"})            
        
        except AttributeError as e:
            return Response(data={"error": str(e)})

        except Exception as e:
            return Response(data={"error": str(e)})



