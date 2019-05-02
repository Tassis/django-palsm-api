from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    profile_count = models.PositiveIntegerField(default=0)
  
    class Meta:
      db_table = "pl_account"
