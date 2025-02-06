# Generated by Django 5.1.5 on 2025-02-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="world",
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
                ("origin_country", models.CharField(max_length=100)),
                ("destination_country", models.CharField(max_length=100)),
                ("number_of_days", models.IntegerField()),
                ("price", models.IntegerField()),
            ],
        ),
    ]
