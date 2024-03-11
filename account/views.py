from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import permission_classes
from drf_spectacular.utils import extend_schema

from .models import User, Address
from .serializers import UserListSerializer, UserCreateSerializer, AddressSerializer
from django.contrib.auth.hashers import make_password



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        request_user =  self.request.user
        if request_user.role == 3:
            return User.objects.all().exclude(pk=request_user.pk)
        else:
            return User.objects.filter(pk=request_user.pk)

@permission_classes([AllowAny])
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        return super().perform_create(serializer)
    

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    

class AddressUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated] 

    @extend_schema(responses=AddressSerializer, request=AddressSerializer)
    def patch(self, request, pk=None, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            instance, created = Address.objects.get_or_create(user=user)
            serializer = AddressSerializer(instance, data=request.data, partial=True,)
            serializer.is_valid(raise_exception=True)
            print(request.data)
            print(serializer.validated_data)
            serializer.save()
            
            # Uaktualnij użytkownika z odnośnikiem do adresu
            user.address = instance
            user.save()
            
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        