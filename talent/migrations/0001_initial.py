# Generated by Django 4.2.2 on 2023-09-26 11:29

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BountyClaim",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "expected_finish_date",
                    models.DateField(default=datetime.date.today),
                ),
                (
                    "kind",
                    models.IntegerField(
                        choices=[
                            (0, "Done"),
                            (1, "Active"),
                            (2, "Failed"),
                            (3, "In review"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "bounty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product_management.bounty",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Person",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("full_name", models.CharField(max_length=256)),
                ("preferred_name", models.CharField(max_length=128)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="avatars/"
                    ),
                ),
                ("headline", models.TextField()),
                ("overview", models.TextField(blank=True)),
                (
                    "location",
                    models.TextField(blank=True, max_length=128, null=True),
                ),
                ("send_me_bounties", models.BooleanField(default=True)),
                (
                    "current_position",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "twitter_link",
                    models.URLField(blank=True, default="", null=True),
                ),
                ("linkedin_link", models.URLField(blank=True, null=True)),
                ("github_link", models.URLField(blank=True, null=True)),
                ("website_link", models.URLField(blank=True, null=True)),
                ("completed_profile", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="person",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "People",
                "db_table": "talent_person",
            },
        ),
        migrations.CreateModel(
            name="Status",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Drone", "Drone"),
                            ("Honeybee", "Honeybee"),
                            ("Trusted Bee", "Trusted Bee"),
                            ("Queen Bee", "Queen Bee"),
                            ("Beekeeper", "Beekeeper"),
                        ],
                        default="Drone",
                        max_length=20,
                    ),
                ),
                ("points", models.PositiveIntegerField(default=0)),
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="status",
                        to="talent.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("active", models.BooleanField(db_index=True, default=False)),
                ("selectable", models.BooleanField(default=False)),
                (
                    "display_boost_factor",
                    models.PositiveSmallIntegerField(default=1),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="talent.skill",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PersonWebsite",
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
                ("website", models.CharField(max_length=200)),
                (
                    "type",
                    models.IntegerField(
                        choices=[(0, "Personal"), (1, "Company")]
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="websites",
                        to="talent.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PersonSkill",
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
                ("skill", models.JSONField(blank=True, null=True)),
                ("expertise", models.JSONField(blank=True, null=True)),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="talent.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IdeaComment",
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
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("text", models.TextField(max_length=1000)),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talent.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("message", models.TextField()),
                (
                    "stars",
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback_provider",
                        to="talent.person",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback_recipient",
                        to="talent.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expertise",
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
                ("selectable", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expertise_children",
                        to="talent.expertise",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skill_expertise",
                        to="talent.skill",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ChallengeComment",
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
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("text", models.TextField(max_length=1000)),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talent.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CapabilityComment",
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
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("text", models.TextField(max_length=1000)),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talent.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BugComment",
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
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("text", models.TextField(max_length=1000)),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talent.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BountyDeliveryAttempt",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "kind",
                    models.IntegerField(
                        choices=[(0, "New"), (1, "Approved"), (2, "Rejected")],
                        default=0,
                    ),
                ),
                ("is_canceled", models.BooleanField(default=False)),
                (
                    "delivery_message",
                    models.CharField(default=None, max_length=2000),
                ),
                (
                    "bounty_claim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="delivery_attempt",
                        to="talent.bountyclaim",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talent.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BountyDeliveryAttachment",
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
                ("file_type", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=100)),
                ("path", models.CharField(max_length=100)),
                (
                    "bounty_delivery_attempt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="talent.bountydeliveryattempt",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bountyclaim",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="talent.person",
            ),
        ),
    ]
