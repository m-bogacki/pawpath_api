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
        fields = ["id","first_name", "last_name", "email", "username", "phone_number", "role", "address"]

class UserCreateSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id","first_name", "last_name", "email", "username", "password", "phone_number", "role"]
    