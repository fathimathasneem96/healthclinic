# Generated by Django 4.2.7 on 2023-12-16 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="Departments")),
            ],
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("age", models.IntegerField(unique=True)),
                ("gender", models.CharField(max_length=6)),
                ("house_name", models.CharField(max_length=200)),
                ("phone_number", models.IntegerField(unique=True)),
                ("description", models.TextField(unique=True)),
            ],
            options={
                "verbose_name": "Patient",
                "verbose_name_plural": "Patients",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Doctors",
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
                ("name", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("qualification", models.CharField(max_length=250)),
                ("image", models.ImageField(blank=True, upload_to="Doctors")),
                ("available", models.BooleanField(default=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Curewell.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "Doctor",
                "verbose_name_plural": "Doctors",
                "ordering": ("name",),
            },
        ),
    ]