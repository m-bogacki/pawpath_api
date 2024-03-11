from django.db import models
from account.models import User
from animals.models import Animal
from django import utils
# Create your models here.




class AnimalCare(models.Model):
    CARE_STATUS_CHOICES = [
        ("New", "New"),
        ("Ongoing", "Ongoing"),
        ("Finished", "Finished")
    ]
    carrer = models.ForeignKey(User, verbose_name="animal_cares", on_delete=models.DO_NOTHING, blank=True, null=True)
    animals = models.ManyToManyField(Animal, related_name='animal_cares')
    start_date = models.DateTimeField(default=utils.timezone.now)
    end_date = models.DateTimeField(default=utils.timezone.now)
    status = models.CharField(default=CARE_STATUS_CHOICES[0][0], choices=CARE_STATUS_CHOICES, max_length=15)
    price = models.IntegerField(blank=True, null=True)


class Offer(models.Model):
    OFFER_STATUS_CHOICES = [
        ("Proposed", "Proposed"),
        ("Accepted", "Accepted"),
        ("Declined", "Declined")
    ]
    
    carrer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(default=OFFER_STATUS_CHOICES[0][0], choices=OFFER_STATUS_CHOICES, max_length=15)
    animal_care = models.ForeignKey(AnimalCare, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="offers")
    description = models.CharField(max_length=255, blank=True, null=True)
    viewed = models.BooleanField(default=False)
    
    
