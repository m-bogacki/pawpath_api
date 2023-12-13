from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from drf_spectacular.utils import extend_schema
from .models import User, Address
from .serializers import UserListSerializer, UserCreateSerializer, AddressSerializer



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

@permission_classes([AllowAny])
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
        
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
    
    
class AddressUpdateAPIView(APIView):

    @extend_schema(responses=AddressSerializer, request=AddressSerializer)
    def patch(self, request, pk=None, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            instance, created = Address.objects.get_or_create(user=user)
            
            serializer = AddressSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            # Uaktualnij użytkownika z odnośnikiem do adresu
            user.address = instance
            user.save()
            
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": f"{e}"})
        