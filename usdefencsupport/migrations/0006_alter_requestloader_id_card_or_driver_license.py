# Generated by Django 5.1.6 on 2025-05-26 12:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usdefencsupport', '0005_alter_requestloader_ssa_1099_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestloader',
            name='id_card_or_driver_license',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
