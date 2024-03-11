# Generated by Django 4.2.5 on 2024-01-11 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal_care", "0023_alter_animalcare_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 11, 15, 32, 47, 151488, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 11, 15, 32, 47, 151292, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
