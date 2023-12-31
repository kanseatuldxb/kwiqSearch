# Generated by Django 4.2.3 on 2023-07-24 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phoneNO', models.IntegerField()),
                ('massageNO', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.JSONField()),
                ('startBudget', models.IntegerField()),
                ('stopBudget', models.IntegerField()),
                ('startCarpetArea', models.IntegerField()),
                ('stopCarpetArea', models.IntegerField()),
                ('possession', models.DateTimeField()),
                ('requirements', models.CharField(max_length=200)),
                ('units', models.JSONField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_API.client')),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('actions', models.CharField(max_length=100)),
                ('date_sent', models.DateTimeField()),
                ('done', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_API.client')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('follow_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_API.followup')),
            ],
        ),
    ]
