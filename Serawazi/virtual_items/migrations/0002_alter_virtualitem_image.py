# Generated by Django 4.2.5 on 2023-09-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualitem',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
