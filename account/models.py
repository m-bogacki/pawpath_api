from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


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
    

