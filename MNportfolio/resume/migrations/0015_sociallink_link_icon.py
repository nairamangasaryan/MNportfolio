# Generated by Django 4.2.2 on 2023-07-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0014_experience_is_current_alter_experience_end_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="sociallink",
            name="link_icon",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
