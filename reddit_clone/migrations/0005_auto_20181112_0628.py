# Generated by Django 2.1.3 on 2018-11-12 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_clone', '0004_auto_20181112_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='redditprofile',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='textpost',
            old_name='subreddit',
            new_name='subreddit_id',
        ),
        migrations.RenameField(
            model_name='textpost',
            old_name='user',
            new_name='user_id',
        ),
    ]