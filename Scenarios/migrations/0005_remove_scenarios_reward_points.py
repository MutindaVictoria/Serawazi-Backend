# Generated by Django 4.2.5 on 2023-10-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scenarios', '0004_scenarios_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenarios',
            name='Reward_points',
        ),
    ]