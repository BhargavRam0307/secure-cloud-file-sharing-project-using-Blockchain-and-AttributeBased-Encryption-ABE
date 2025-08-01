# Generated by Django 5.1.7 on 2025-04-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileLink', models.TextField()),
                ('uploaders', models.JSONField(default=list)),
                ('iv', models.BinaryField()),
                ('cipher_key', models.BinaryField()),
                ('access_policy', models.JSONField(default=list)),
                ('coefficients', models.BinaryField()),
                ('request_ids', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=80)),
                ('department', models.CharField(max_length=255)),
                ('subscription_period', models.CharField(max_length=100)),
                ('private_key', models.CharField(blank=True, max_length=66, null=True)),
            ],
        ),
    ]
