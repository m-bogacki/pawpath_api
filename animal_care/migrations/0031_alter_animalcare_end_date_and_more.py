# Generated by Django 4.2.5 on 2024-02-01 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "animal_care",
            "0030_alter_animalcare_carrer_alter_animalcare_end_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcare",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 1, 22, 6, 44, 137858, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="animalcare",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 1, 22, 6, 44, 137676, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
