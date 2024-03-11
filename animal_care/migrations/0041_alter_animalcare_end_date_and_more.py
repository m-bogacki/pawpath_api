# Generated by Django 4.2.5 on 2024-02-13 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal_care", "0040_alter_animalcare_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 13, 19, 54, 44, 49072, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 13, 19, 54, 44, 48870, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
