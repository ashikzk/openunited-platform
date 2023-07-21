# Generated by Django 4.2.2 on 2023-07-15 17:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_logged', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default='', max_length=39, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username may only contain letters and numbers', regex='^[a-z0-9]*$')])),
            ],
            options={
                'db_table': 'users_user',
            },
        ),
        migrations.CreateModel(
            name='BlacklistedUsernames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'black_listed_usernames',
            },
        ),
        migrations.CreateModel(
            name='OrganisationPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('right', models.IntegerField(choices=[(0, 'Follower'), (1, 'Admin'), (2, 'Manager'), (3, 'Contributor')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('organisation', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='commerce.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]