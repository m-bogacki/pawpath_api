# Generated by Django 4.2.5 on 2023-09-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0002_animal_delete_dog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="specie",
            field=models.CharField(
                choices=[("Dog", "Dog"), ("Cat", "Cat")], max_length=10
            ),
        ),
    ]
