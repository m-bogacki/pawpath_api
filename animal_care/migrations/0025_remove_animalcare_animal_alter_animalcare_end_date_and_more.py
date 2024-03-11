# Generated by Django 4.2.5 on 2024-01-15 21:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0021_alter_animal_size"),
        ("animal_care", "0024_alter_animalcare_end_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="animalcare", name="animal",),
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 15, 21, 22, 50, 295080, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 15, 21, 22, 50, 294884, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="AnimalCarePets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="animals.animal",
                        verbose_name="animal_care_pets_animal",
                    ),
                ),
                (
                    "animal_care",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="animal_care.animalcare",
                        verbose_name="animal_care_pets_animal_care",
                    ),
                ),
            ],
        ),
    ]
