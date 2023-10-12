from django.db import models
from account.models import User
# Create your models here.

class AnimalCare(models.Model):
    carrer = models.ForeignKey(User, verbose_name="animal_care_carrer", on_delete=models.DO_NOTHING)