from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnimalListSerializer, AnimalCreateSerializer ,CareInstructionsSerializer


from .models import Animal, CareInstructions
from account.models import User


# Create your views here.


class AnimalCreate(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalCreateSerializer
    permission_classes = [IsAuthenticated]



class AnimalList(generics.ListAPIView):
    serializer_class = AnimalListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        base_user = self.request.user
        try:
            user = User.objects.get(pk=base_user.pk)
            if user.role != 3:
                return Animal.objects.filter(owner=user)
            else:
                return Animal.objects.all()
        except:
            return Animal.objects.all()


class AnimalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalListSerializer
    permission_classes = [IsAuthenticated]


    
    def get_serializer_class(self):
        if self.request.method == "PATCH" or self.request.method == "PUT":
            return AnimalCreateSerializer
        return AnimalListSerializer
    
    def get_queryset(self):
        base_user = self.request.user
        try:
            user = User.objects.get(pk=base_user.pk)
            if user.role != 3:
                return Animal.objects.filter(owner=user)
            else:
                return Animal.objects.all()
        except:
            return Animal.objects.all()
  
    
class CareInstructionsUpdate(APIView):
    permission_classes = [IsAuthenticated]
    
    @extend_schema(responses=CareInstructionsSerializer, request=CareInstructionsSerializer)
    def patch(self, request, pk=None):
        animal = Animal.objects.get(pk=pk)
        instance = CareInstructions.objects.filter(animal=animal).first()
        if not instance:
            return Response({"detail": "CareInstructions not found for the specified animal."}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = CareInstructionsSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        