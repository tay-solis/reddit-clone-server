from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class TextPost(models.Model):
    tag_line = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    thumbnail_image_url = models.TextField()
    votes = models.IntegerField()

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_comments')
    post_id = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name = 'post_comments')
    votes = models.IntegerField()
    content = models.TextField()
