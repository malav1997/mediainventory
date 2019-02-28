from django.db import models
from django.contrib.auth.models import AbstractUser

"""Extending the django inbuilt user model.
This model contains the user information"""

class UserProfile(AbstractUser):
    SUPERUSER = 'superuser'
    CHANNELADMIN = 'channel_admin'
    CLIENT = 'client'
    USER_CHOICES = (
        (SUPERUSER, 'Supeuser'),
        (CHANNELADMIN, 'Channel Admin'),
        (CLIENT, 'Client'),
    )
    user_role = models.CharField(max_length=30, choices=USER_CHOICES, default=CLIENT)
    cell_no = models.BigIntegerField(null=True)


