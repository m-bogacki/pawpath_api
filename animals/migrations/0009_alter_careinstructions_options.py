# Generated by Django 4.2.5 on 2023-09-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0008_careinstructions_animal_care_instructions"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="careinstructions", options={"verbose_name": "Care Instructions"},
        ),
    ]
