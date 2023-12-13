# Generated by Django 4.2.5 on 2023-11-09 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal_care", "0004_alter_animalcare_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 9, 12, 50, 18, 597558, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 9, 12, 50, 18, 597353, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
