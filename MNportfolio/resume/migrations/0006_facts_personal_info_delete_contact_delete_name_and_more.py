# Generated by Django 4.2.2 on 2023-07-08 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0005_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Facts",
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
                ("happy_clients_count", models.PositiveIntegerField()),
                (
                    "happy_clients_description",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
                ("projects_count", models.PositiveIntegerField()),
                (
                    "projects_description",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
                ("awards_count", models.PositiveIntegerField()),
                (
                    "awards_description",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
                ("years_of_exreiance", models.PositiveIntegerField(max_length=2)),
                (
                    "years_of_exreiance_description",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Personal_info",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=15)),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[django.core.validators.EmailValidator],
                    ),
                ),
                ("city", models.CharField(max_length=40)),
                ("age", models.PositiveIntegerField(max_length=2)),
                ("degree", models.CharField(max_length=20)),
                ("freelance", models.CharField(max_length=20)),
                (
                    "github",
                    models.URLField(validators=[django.core.validators.URLValidator]),
                ),
                ("short_resume", models.TextField(max_length=250)),
                ("sumary_name", models.CharField(max_length=30)),
                ("sumary_description", models.TextField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.DeleteModel(
            name="Name",
        ),
        migrations.DeleteModel(
            name="ShortResume",
        ),
        migrations.DeleteModel(
            name="Sumary",
        ),
        migrations.AlterField(
            model_name="hardskill",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="language",
            name="level",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="language",
            name="name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="skill",
            name="name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="skill",
            name="value",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="sociallink",
            name="link",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="sociallink",
            name="link_name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="softskill",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
