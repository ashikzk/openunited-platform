# Generated by Django 4.2.2 on 2024-05-28 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("talent", "0011_alter_bountydeliveryattempt_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PersonWebsite",
        ),
    ]