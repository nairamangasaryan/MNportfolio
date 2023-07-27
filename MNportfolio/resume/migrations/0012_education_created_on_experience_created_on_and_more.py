# Generated by Django 4.2.2 on 2023-07-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0011_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="experience",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="facts",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="hardskill",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="language",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="personal_info",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="service",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="skill",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="sociallink",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="softskill",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]