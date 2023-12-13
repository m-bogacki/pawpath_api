# Generated by Django 4.2.5 on 2023-12-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0011_rename_postalcode_address_postal_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=99.99, null=True
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=99.99, null=True
            ),
        ),
    ]
