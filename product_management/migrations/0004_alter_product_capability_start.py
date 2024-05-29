# Generated by Django 4.2.2 on 2023-10-22 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0003_alter_product_full_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="capability_start",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="product_management.capability",
            ),
        ),
    ]
