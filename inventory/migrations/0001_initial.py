# Generated by Django 4.2.7 on 2023-11-28 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=10)),
                ('number', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
                ('f_birth', models.DateField(default=datetime.date.today)),
                ('creation_at', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=50)),
                ('Disease_history', models.TextField(blank=True)),
            ],
        ),
    ]