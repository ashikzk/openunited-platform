# Generated by Django 4.2.2 on 2024-05-14 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product_management", "0030_delete_ideavote"),
        ("talent", "0006_remove_bountyclaim_kind_bountyclaim_status"),
        ("security", "0004_alter_signuprequest_successful"),
    ]

    operations = [
        migrations.CreateModel(
            name="IdeaVote",
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
                ("voted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "idea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product_management.idea",
                    ),
                ),
                (
                    "voter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talent.person",
                    ),
                ),
            ],
            options={
                "unique_together": {("voter", "idea")},
            },
        ),
    ]
