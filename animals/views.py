from drf_spectacular.utils import extend_schema

# Create your views here.
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal, CareInstructions
from .serializers import AnimalListSerializer, AnimalCreateSerializer, CareInstructionsSerializer


# Create your views here.


class AnimalCreate(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalCreateSerializer


class AnimalList(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializer


class AnimalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializer
    
class CareInstructionsUpdate(APIView):

    @extend_schema(responses=CareInstructionsSerializer, request=CareInstructionsSerializer)
    def patch(self, request, pk=None, *args, **kwargs):
        animal = Animal.objects.get(pk=pk)
        instance = CareInstructions.objects.filter(animal=animal).first()
        if not instance:
            return Response({"detail": "CareInstructions not found for the specified animal."}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = CareInstructionsSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        