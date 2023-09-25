from django.db import models

# Create your models here.


class Animal(models.Model):
    ANIMAL_CHOICES = (
        ("Dog", "Dog"),
        ("Cat", "Cat"),
    )
    
    name = models.CharField(max_length=60)
    specie = models.CharField(choices=ANIMAL_CHOICES, max_length=10)

    
    