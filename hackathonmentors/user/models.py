from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Overrides Django's basic AbstractUser class if needed
Reference: https://github.com/django/django/blob/master/django/contrib/auth/models.py
"""


class CustomUser(AbstractUser):

    class Meta:
        db_table = 'users'
