# Generated by Django 4.2.5 on 2023-09-30 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("animals", "0014_alter_animal_care_instructions_alter_animal_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="care_instructions",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="animals.careinstructions",
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
