from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class RedditProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_profile')
    display_name = models.CharField(max_length=25, blank=True)
    bio = models.TextField()
    karma = models.IntegerField()
    icon_url = models.TextField()
    def natural_key(self):
        return dict(
            user = self.user_id.natural_key(), 
            display_name = self.display_name,
            bio = self.bio,
            karma = self.karma,
            icon_url = self.icon_url
        )

    def to_json(self):
        return dict(
            user = self.user_id.natural_key(), 
            display_name = self.display_name,
            bio = self.bio,
            karma = self.karma,
            icon_url = self.icon_url
        )
    
    
class SubReddit(models.Model):
    name= models.CharField(max_length=100, blank=True)
    slug= models.CharField(max_length=100, blank=True)

    def natural_key(self):
        return dict(
            name = self.name, 
            slug = self.slug)

class TextPost(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_posts')
    subreddit_id = models.ForeignKey(SubReddit, on_delete=models.CASCADE, related_name = 'subreddit_posts')
    tag_line = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    thumbnail_image_url = models.TextField()
    votes = models.IntegerField()
    def natural_key(self):
        return dict(
            user = self.user_id.natural_key(), 
            subreddit = self.subreddit_id.natural_key(), 
            tag_line = self.tag_line, 
            content = self.content, 
            thumbnail_image_url = self.thumbnail_image_url, 
            votes = self.votes)

    def to_json(self):
        return dict(
            user=self.user_id.natural_key(),
            subreddit=self.subreddit_id.natural_key(),
            tag_line = self.tag_line,
            content = self.content,
            thumbnail_image_url = self.thumbnail_image_url,
            votes=self.votes
        )

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_comments')
    post_id = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name = 'user_comments')
    votes = models.IntegerField()
    content = models.TextField()
    def to_json(self):
        return dict(
            user=[self.user_id.natural_key()],
            post=[self.post_id.natural_key()],
            content = self.content,
            votes=self.votes
        )
