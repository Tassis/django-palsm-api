from django.db import models
from django.utils import timezone
from profiles.models import Profile
# Create your models here.
class Page(models.Model):

    page_id = models.AutoField(unique=True, primary_key=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pages', default=None)
    url = models.URLField()
    identifier = models.TextField()
    title = models.TextField(default=None)
    comment_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'pl_pages'