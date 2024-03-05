from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, verbose_name='User\'s email', unique=True)
    password = models.CharField(max_length=255, verbose_name='User\'s password')
    username = models.CharField(max_length=255, verbose_name='User\'s username', unique=True)
    phone = PhoneNumberField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'email', 'phone']
