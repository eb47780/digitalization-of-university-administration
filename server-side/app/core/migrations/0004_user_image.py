# Generated by Django 2.1.15 on 2022-01-24 18:51

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220124_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.user_image_file_path),
        ),
    ]
