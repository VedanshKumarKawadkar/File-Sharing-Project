from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
import uuid
# Create your models here.


class UserDetails(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    files_keys = models.TextField(verbose_name="file keys")
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.username


class FileDetails(models.Model):
    files = models.FileField()
    filename = models.TextField(verbose_name="file name", default="file")
    uploaded_date = models.DateTimeField(verbose_name="upload date", auto_now_add=True)
    uploaded_by = models.CharField(max_length=15)
    file_key = models.UUIDField(verbose_name="file id", unique=True, default=uuid.uuid4())

    def __str__(self):
        return self.filename