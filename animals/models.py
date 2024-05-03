from django.db import models
from account.models import User
from django.core.exceptions import ValidationError

# Create your models here.

SIZE_CHOICES = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Big", "Big"),
        ("Very Big", "Very Big")
    )


def validate_number_of_walks(number_of_walks):
    if number_of_walks < 2 or number_of_walks > 4:
        raise ValidationError(
            f"{number_of_walks} must can be set from 2 to 4"
        )

def calc_animal_size(weight: float):
    size = SIZE_CHOICES[0][0]
    if weight > 8:
        size = SIZE_CHOICES[1][0]
    if weight > 20:
        size = SIZE_CHOICES[2][0]
    if weight > 35:
        size = SIZE_CHOICES[3][0]
    return size

class CareInstructions(models.Model):
    number_of_walks_per_day = models.IntegerField(
        verbose_name="Number of walks per day",
        default=3, validators=[validate_number_of_walks], blank=True)
    food_portions = models.IntegerField(default=3, blank=True)
    food_amount = models.IntegerField(blank=True,null=True)
    additional_instructions = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Care Instructions"


def file_location(instance, filename, **kwargs):
    return f"images/animals/{instance.owner.username}/{instance.name}"

class Animal(models.Model):
    ANIMAL_CHOICES = (
        ("Dog", "Dog"),
        ("Cat", "Cat"),
    )


    image = models.ImageField(upload_to=file_location, blank=True, null=True)
    name = models.CharField(max_length=60)
    species = models.CharField(choices=ANIMAL_CHOICES, max_length=10, default=ANIMAL_CHOICES[0])
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=False, related_name="animals")
    weight = models.DecimalField(decimal_places=1, max_digits=4, null=True, blank=True)
    size = models.CharField(max_length=12,choices=SIZE_CHOICES, null=True, blank=True)
    care_instructions = models.OneToOneField(CareInstructions, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if self.care_instructions is None:
            animal_care_instructions = CareInstructions.objects.create()
            self.care_instructions = animal_care_instructions

        self.size = calc_animal_size(self.weight)
        super(Animal, self).save(*args,**kwargs)
