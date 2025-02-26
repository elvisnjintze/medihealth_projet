# Generated by Django 4.2.17 on 2024-12-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CMPPAR",
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
                ("CODPAR", models.CharField(max_length=10)),
                ("CLE", models.CharField(max_length=3)),
                ("LIBPAR", models.CharField(max_length=30)),
                ("MEMO", models.CharField(blank=True, max_length=255, null=True)),
                ("VALC", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "VALN",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=16, null=True
                    ),
                ),
                (
                    "VALT",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("DATE_CREAT", models.DateField()),
                ("UTIL_CREAT", models.CharField(max_length=5)),
                ("DATE_MODIF", models.DateField(blank=True, null=True)),
                ("UTIL_MODIF", models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                "verbose_name": "CMPPAR",
                "verbose_name_plural": "CMPPARs",
                "db_table": "CMPPAR",
                "managed": True,
                "unique_together": {("CODPAR", "CLE")},
            },
        ),
    ]
