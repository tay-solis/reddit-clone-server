from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class RedditProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_profile')
    bio = models.TextField()
    karma = models.IntegerField()
    icon_url = models.TextField()

    
class SubReddit(models.Model):
    name= models.CharField(max_length=100, blank=True)
    slug= models.CharField(max_length=100, blank=True)

class TextPost(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_posts')
    subreddit_id = models.ForeignKey(SubReddit, on_delete=models.CASCADE, related_name = 'subreddit_posts')
    tag_line = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    thumbnail_image_url = models.TextField()
    votes = models.IntegerField()

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_comments')
    post_id = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name = 'user_comments')
    votes = models.IntegerField()
    content = models.TextField()
