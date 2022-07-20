from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=75, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)