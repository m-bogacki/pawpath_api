from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]
        
    def create(self, validated_data):
        hash_password = make_password(validated_data.pop('password'))
        user = User.objects.create(password=hash_password,**validated_data)
        return user