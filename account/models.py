from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=15)


class User(AbstractUser):
    CARRER = 1
    OWNER = 2
    ADMIN = 3
    
    
    ROLE_CHOICES =(
        (CARRER, 'Carrer'),
        (OWNER, 'Owner'),
        (ADMIN, 'Admin')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    

