# Generated by Django 4.2.5 on 2023-09-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Animal",
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
                ("name", models.CharField(max_length=60)),
                (
                    "specie",
                    models.CharField(choices=[(1, "Dog"), (2, "Cat")], max_length=10),
                ),
            ],
        ),
        migrations.DeleteModel(name="Dog",),
    ]
