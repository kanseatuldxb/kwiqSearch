# Generated by Django 4.2.3 on 2023-07-22 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_API', '0007_project1_unit1_remove_unit_project_delete_project_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project1',
            new_name='Project',
        ),
        migrations.RenameModel(
            old_name='Unit1',
            new_name='Unit',
        ),
    ]
