# Generated by Django 3.1.7 on 2022-03-06 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0004_auto_20220306_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='filedetails',
            name='file_key',
            field=models.UUIDField(default=uuid.UUID('abe9db33-26a8-4e11-92f5-3829ac6fa34b'), unique=True, verbose_name='file id'),
        ),
    ]