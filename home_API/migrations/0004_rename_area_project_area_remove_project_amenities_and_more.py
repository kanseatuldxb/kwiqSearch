# Generated by Django 4.2.3 on 2023-07-22 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_API', '0003_rename_carpetarea_unit_carpetarea_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='area',
            new_name='Area',
        ),
        migrations.RemoveField(
            model_name='project',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='project',
            name='areaIn',
        ),
        migrations.RemoveField(
            model_name='project',
            name='availableUnit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='bhk',
        ),
        migrations.RemoveField(
            model_name='project',
            name='brokerage',
        ),
        migrations.RemoveField(
            model_name='project',
            name='carpetArea',
        ),
        migrations.RemoveField(
            model_name='project',
            name='contactNumber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='contactPerson',
        ),
        migrations.RemoveField(
            model_name='project',
            name='developerName',
        ),
        migrations.RemoveField(
            model_name='project',
            name='flatsPerFloors',
        ),
        migrations.RemoveField(
            model_name='project',
            name='floors',
        ),
        migrations.RemoveField(
            model_name='project',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='project',
            name='incentive',
        ),
        migrations.RemoveField(
            model_name='project',
            name='landParcel',
        ),
        migrations.RemoveField(
            model_name='project',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='project',
            name='lifts',
        ),
        migrations.RemoveField(
            model_name='project',
            name='location',
        ),
        migrations.RemoveField(
            model_name='project',
            name='marketValue',
        ),
        migrations.RemoveField(
            model_name='project',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='project',
            name='possession',
        ),
        migrations.RemoveField(
            model_name='project',
            name='power',
        ),
        migrations.RemoveField(
            model_name='project',
            name='price',
        ),
        migrations.RemoveField(
            model_name='project',
            name='projectName',
        ),
        migrations.RemoveField(
            model_name='project',
            name='projectType',
        ),
        migrations.RemoveField(
            model_name='project',
            name='readyToMove',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rera',
        ),
        migrations.RemoveField(
            model_name='project',
            name='totalUnit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='transport',
        ),
        migrations.RemoveField(
            model_name='project',
            name='waterSupply',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='carpetArea',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='price',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='unit',
        ),
        migrations.AlterField(
            model_name='unit',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_API.project'),
        ),
    ]