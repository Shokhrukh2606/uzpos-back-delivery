from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone=models.CharField(max_length=9, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone