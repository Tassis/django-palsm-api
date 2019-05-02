from django.db import models
from profiles.models import Profile
from pages.models import Page
from django.utils import timezone
# Create your models here.
class Comment(models.Model):

    comment_id = models.AutoField(db_index=True, primary_key=True)
    profile_id = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
    page_id = models.ForeignKey(Page, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_member = models.BooleanField(default=False)

    class Meta:
        db_table = 'pl_comments'