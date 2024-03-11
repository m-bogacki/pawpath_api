# Generated by Django 4.2.5 on 2024-02-13 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal_care", "0041_alter_animalcare_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 13, 21, 13, 15, 897134, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 13, 21, 13, 15, 896948, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
