# Generated by Django 4.0.4 on 2022-06-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='upload/default.png', null=True, upload_to=''),
        ),
    ]
