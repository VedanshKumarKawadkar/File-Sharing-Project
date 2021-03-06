# Generated by Django 3.1.7 on 2022-03-06 08:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0005_auto_20220306_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedetails',
            name='file_key',
            field=models.UUIDField(default=uuid.UUID('422d50b5-81cd-456d-8038-1d748697fbe3'), unique=True, verbose_name='file id'),
        ),
    ]
