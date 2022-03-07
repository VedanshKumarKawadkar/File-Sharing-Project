from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):  
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserDetails(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    received_files_keys = models.TextField(verbose_name="file keys", default="")
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perm(self, app_label):
        return True

class FileDetails(models.Model):
    files = models.FileField()
    filename = models.TextField(verbose_name="file name", default="file")
    uploaded_date = models.DateTimeField(verbose_name="upload date", auto_now_add=True)
    uploaded_by = models.CharField(max_length=15)
    file_key = models.CharField(verbose_name="file id", unique=True, max_length=50, primary_key=True)

    def __str__(self):
        return self.filename