# Generated by Django 4.0.4 on 2022-06-08 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0006_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]