# Generated by Django 3.2.12 on 2023-09-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scenarios', '0004_alter_scenarios_reward_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarios',
            name='scenario_title',
            field=models.TextField(max_length=255),
        ),
    ]
