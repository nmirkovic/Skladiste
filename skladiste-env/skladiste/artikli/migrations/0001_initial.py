# Generated by Django 4.1.7 on 2023-03-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artikl",
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
                (
                    "naziv_artikla",
                    models.CharField(max_length=30, verbose_name="naziv artikla"),
                ),
                (
                    "opis_artikla",
                    models.CharField(max_length=30, verbose_name="opis artikla"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JedinicaMjere",
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
                (
                    "naziv_mjere",
                    models.CharField(max_length=25, verbose_name="naziv mjere"),
                ),
                ("oznaka", models.CharField(max_length=5, verbose_name="oznaka")),
            ],
        ),
        migrations.CreateModel(
            name="Lokacija",
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
                (
                    "naziv_lokacije",
                    models.CharField(max_length=5, verbose_name="naziv lokacije"),
                ),
                (
                    "opis_lokacije",
                    models.CharField(max_length=100, verbose_name="opis lokacije"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stanje",
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
                ("kolicina", models.IntegerField(null=True)),
                (
                    "artikl_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="artikli.artikl"
                    ),
                ),
                (
                    "jedinica_mjere_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="artikli.jedinicamjere",
                    ),
                ),
                (
                    "lokacija_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="artikli.lokacija",
                    ),
                ),
            ],
        ),
    ]
