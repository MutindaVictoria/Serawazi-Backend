# Generated by Django 3.2.12 on 2023-09-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenario_collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenariocollection',
            name='total_Scenarios',
            field=models.IntegerField(default=5),
        ),
    ]