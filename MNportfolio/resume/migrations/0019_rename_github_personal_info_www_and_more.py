# Generated by Django 4.2.2 on 2023-07-14 22:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0018_rename_job_discribtion_experience_job_discription_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personal_info",
            old_name="github",
            new_name="www",
        ),
        migrations.AlterField(
            model_name="experience",
            name="job_discription",
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
