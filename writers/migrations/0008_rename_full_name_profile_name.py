# Generated by Django 4.0.4 on 2022-06-11 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0007_remove_profile_location_delete_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='full_name',
            new_name='name',
        ),
    ]
