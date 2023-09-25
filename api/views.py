from rest_framework import generics
from animals.models import Animal
from animals.serializers import AnimalSerializer
from rest_framework.response import Response
# Create your views here.


class AnimalList(generics.ListAPIView):
    queryset = Animal.objects.all()
    
    """
    That's an api endpoint that returns all dogs
    """
    def list(self, request):
        self.queryset = self.queryset.filter()
        serializer = AnimalSerializer(self.queryset, many=True)
        return Response(serializer.data)