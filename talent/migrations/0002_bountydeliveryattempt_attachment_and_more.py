# Generated by Django 4.2.2 on 2023-10-12 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("talent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bountydeliveryattempt",
            name="attachment",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name="bounty_delivery_attempts/",
            ),
        ),
        migrations.AlterField(
            model_name="bountydeliveryattempt",
            name="bounty_claim",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="delivery_attempt",
                to="talent.bountyclaim",
            ),
        ),
        migrations.AlterField(
            model_name="bountydeliveryattempt",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.person"
            ),
        ),
        migrations.DeleteModel(
            name="BountyDeliveryAttachment",
        ),
    ]
