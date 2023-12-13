from rest_framework.serializers import ModelSerializer, CharField
from .models import User, Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ["id"]


class UserListSerializer(ModelSerializer):
    address = AddressSerializer(read_only=True)
    
    class Meta:
        model = User
        exclude = ["user_permissions", "groups", "password", "is_staff", "first_name", "is_superuser", "last_login"]

class UserCreateSerializer(ModelSerializer):
    address = AddressSerializer(read_only=True)
    
    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]

