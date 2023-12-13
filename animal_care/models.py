from django.db import models
from account.models import User
from animals.models import Animal
from django.utils import timezone
# Create your models here.




class AnimalCare(models.Model):

    CARE_STATUS_CHOICES = [
        ("New", "New"),
        ("Ongoing", "Ongoing"),
        ("Finished", "Finished")
    ]
    
    carrer = models.ForeignKey(User, verbose_name="animal_care_carrer", on_delete=models.DO_NOTHING, blank=True, null=True)
    animal = models.ForeignKey(Animal, verbose_name="animal_care_animals", on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(default=timezone.now())
    status = models.CharField(default=CARE_STATUS_CHOICES[0], choices=CARE_STATUS_CHOICES, max_length=15)



class Offer(models.Model):
    
    OFFER_STATUS_CHOICES = [
        ("Proposed", "Proposed"),
        ("Accepted", "Accepted"),
        ("Declined", "Declined")
    ]
    
    carrer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(default=OFFER_STATUS_CHOICES[0], choices=OFFER_STATUS_CHOICES, max_length=15)
    animal_care = models.ForeignKey(AnimalCare, blank=True, null=True, on_delete=models.DO_NOTHING)
    
    
