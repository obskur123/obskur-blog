# Generated by Django 4.2.6 on 2023-12-05 14:47

import blog.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(storage=blog.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
