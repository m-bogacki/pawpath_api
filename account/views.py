from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .models import User
from .serializers import UserListSerializer, UserCreateSerializer



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    
    def list(self, request):
        self.queryset = self.queryset.filter()
        serializer = UserListSerializer(self.queryset ,many=True)
        
        return Response(data=serializer.data)

@permission_classes([AllowAny])
class UserCreateView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = UserCreateSerializer(data=request.data)
            username = request.data.get('username')
            if not username:
                return Response(data={'data':'Username is required field'})

            existing_user = User.objects.get(username=username)
            if existing_user:
                return Response(data={'data':'User with this username already exists'})
            
            email = request.data.get('email')
            existing_user = User.objects.get(email=email)
            if existing_user:
                return Response(data={'data':'User with this username already exists'})
            
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': str(e)})
        
        
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    def retrieve(self, request, id):
        self.queryset = self.queryset.get(id=id)
        return Response(data=UserListSerializer(self.queryset).data)
        
        
    def partial_update(self, request, id, *args, **kwargs):
        data = request.data
        user = User.objects.get(id=id)
        serializer = UserCreateSerializer(user, data=data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)