# Generated by Django 4.2.5 on 2024-02-13 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal_care", "0043_alter_animalcare_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 13, 21, 26, 2, 173237, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 13, 21, 26, 2, 173065, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
