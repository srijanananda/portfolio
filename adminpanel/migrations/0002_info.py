# Generated by Django 5.1.4 on 2025-06-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Info",
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
                ("name", models.CharField(max_length=100)),
                ("subtitle", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("location", models.CharField(max_length=255)),
                ("summary", models.TextField()),
                ("work_title", models.CharField(max_length=255)),
                ("work_project", models.CharField(max_length=255)),
                ("work_duration", models.CharField(max_length=100)),
                ("work_description", models.TextField()),
                ("skills_programming", models.TextField()),
                ("skills_web", models.TextField()),
                ("skills_db", models.TextField()),
                ("skills_vc", models.TextField()),
                ("skills_ai", models.TextField()),
                ("skills_embedded", models.TextField()),
                ("education_degree", models.CharField(max_length=255)),
                ("education_college", models.CharField(max_length=255)),
                ("education_graduation", models.CharField(max_length=100)),
            ],
        ),
    ]
