# Generated by Django 4.2.2 on 2024-03-23 15:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0014_rename_capability_productarea_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductTree",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID(
                            "09332c8a-0484-43c7-b283-42e07798686e"
                        ),
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_trees",
                        to="product_management.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productarea",
            name="product_tree",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product_areas",
                to="product_management.producttree",
            ),
        ),
    ]
