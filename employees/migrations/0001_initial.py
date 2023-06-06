# Generated by Django 4.2.2 on 2023-06-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=32)),
                ("last_name", models.CharField(max_length=32)),
                ("mobile_number", models.CharField(max_length=20)),
                ("start_date", models.DateField()),
                ("salary", models.CharField(max_length=20)),
                ("employee_id", models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
