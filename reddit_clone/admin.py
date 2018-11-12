from django.contrib import admin
from .models import TextPost, Comment, SubReddit, RedditProfile

# Register your models here.
admin.site.register(SubReddit)
admin.site.register(TextPost)
admin.site.register(Comment)
admin.site.register(RedditProfile)