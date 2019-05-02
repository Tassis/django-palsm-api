from django.db import models
from accounts.models import Account
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Account, related_name='profile', on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=60, unique=True)
    page_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    comment_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'pl_profiles'
