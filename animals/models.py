from django.db import models
from account.models import User
from django.core.exceptions import ValidationError

# Create your models here.


def validate_number_of_walks(number_of_walks):
    if number_of_walks < 2 or number_of_walks > 4:
        raise ValidationError(
            f"{number_of_walks} must can be set from 2 to 4"
        )


class CareInstructions(models.Model):
    number_of_walks_per_day = models.IntegerField(
        verbose_name="Number of walks per day",
        null=True,
        blank=True,
        default=3, validators=[validate_number_of_walks])

    def create(self, validated_data):
        return CareInstructions.objects.create(**validated_data)

    class Meta:
        verbose_name = "Care Instructions"


class Animal(models.Model):
    ANIMAL_CHOICES = (
        ("Dog", "Dog"),
        ("Cat", "Cat"),
    )

    name = models.CharField(max_length=60)
    species = models.CharField(choices=ANIMAL_CHOICES, max_length=10, default=ANIMAL_CHOICES[0])
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
    care_instructions = models.OneToOneField(CareInstructions, on_delete=models.CASCADE, null=True, blank=True)
