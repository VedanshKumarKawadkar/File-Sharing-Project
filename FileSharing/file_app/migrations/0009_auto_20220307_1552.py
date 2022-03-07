# Generated by Django 3.1.7 on 2022-03-07 10:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0008_auto_20220307_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filedetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='filedetails',
            name='file_key',
            field=models.UUIDField(default=uuid.UUID('b70d7bce-6077-475b-b3f3-5880770e122f'), primary_key=True, serialize=False, unique=True, verbose_name='file id'),
        ),
    ]