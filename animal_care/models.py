from django.db import models
from account.models import User
from animals.models import Animal
from django.utils import timezone
# Create your models here.

class AnimalCare(models.Model):
    carrer = models.ForeignKey(User, verbose_name="animal_care_carrer", on_delete=models.PROTECT)
    animal = models.ForeignKey(Animal, verbose_name="animal_care_animals", on_delete=models.PROTECT)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(default=timezone.now())
    
    