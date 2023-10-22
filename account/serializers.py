from rest_framework.serializers import ModelSerializer
from .models import User, Address
from django.contrib.auth.hashers import make_password

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class UserListSerializer(ModelSerializer):
        class Meta:
            model = User
            exclude = ["user_permissions", "groups", "password", "is_staff"]

class UserCreateSerializer(ModelSerializer):
    address = AddressSerializer(read_only=True)
    
    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]
        
    def create(self, validated_data):
        hash_password = make_password(validated_data.pop('password'))
        user_role = validated_data.get('role')
        user = User.objects.create(password=hash_password,
                                    is_superuser = True if user_role is 3 else False,
                                    **validated_data
                                )
        return user
    

    