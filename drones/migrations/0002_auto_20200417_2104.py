# Generated by Django 3.0.5 on 2020-04-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='dronecategory',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
    ]
