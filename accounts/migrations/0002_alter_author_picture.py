# Generated by Django 3.2.6 on 2022-06-16 08:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Picture'),
        ),
    ]
