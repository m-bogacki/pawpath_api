from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer



class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    
    def list(self, request):
        self.queryset = self.queryset.filter()
        serializer = UserSerializer(self.queryset ,many=True)
        
        return Response(data=serializer.data)


    def create(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                existing_user = User.objects.filter(username=serializer.validated_data.get('username')).first()
                print(existing_user)
                serializer.save()
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': str(e)})