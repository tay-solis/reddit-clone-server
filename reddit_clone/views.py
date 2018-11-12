from django.shortcuts import render
from .models import TextPost, Comment, RedditProfile, SubReddit
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models import F
from django.contrib.auth.models import User

####### FRONT PAGE #######
def all_posts(request):
    posts = TextPost.objects.all().values()
    posts = list(posts) 
    return JsonResponse(posts, safe=False)

####### POSTS VIEWS #######
# GET all posts from subreddit
def all_posts_from(request, slug):
    subreddit = SubReddit.objects.get(slug=slug)
    posts = serializers.serialize('json', TextPost.objects.filter(subreddit_id = subreddit.id))
    return HttpResponse(posts, content_type='json')

# GET one post by id
def post_detail(request, pk):
    post = TextPost.objects.filter(id=pk).values()
    post = list(post) 
    return JsonResponse(post, safe=False)

# POST add a vote to a post
def post_add_vote(request, pk):
    post = TextPost.objects.filter(id=pk)
    user = post[0].user_id
    profile = RedditProfile.objects.filter(user_id = user.id)
    profile.update(karma=F('karma') + 1)
    post.update(votes=F('votes') + 1)
    updated_post = serializers.serialize('json', post)
    return HttpResponse(updated_post, content_type='json')

# POST minus a vote to a post
def post_minus_vote(request, pk):
    post = TextPost.objects.filter(id=pk)
    user = post[0].user_id
    profile = RedditProfile.objects.filter(user_id = user.id)
    profile.update(karma=F('karma') - 1)
    post.update(votes=F('votes') - 1)
    updated_post = serializers.serialize('json', post)
    return HttpResponse(updated_post, content_type='json')

####### COMMENT VIEWS ########
# GET all comments on a post
def post_comments(request, post_id):
    post_comments = serializers.serialize('json', Comment.objects.filter(post_id=post_id))
    return HttpResponse(post_comments, content_type='json')

#GET comment by id
def comment_detail(request, post_id, comment_id):
    comment = Comment.objects.filter(post_id = post_id, id=comment_id).values()
    comment = list(comment) 
    return JsonResponse(comment, safe=False)

#POST add a vote to a comment
def comment_add_vote(request, post_id, comment_id):
    comment = Comment.objects.filter(post_id = post_id, id=comment_id)
    user = comment[0].user_id
    profile = RedditProfile.objects.filter(user_id = user.id)
    profile.update(karma=F('karma') + 1)
    comment.update(votes=F('votes') + 1)
    updated_comment = serializers.serialize('json', comment)
    return HttpResponse(updated_comment, content_type='json')

#POST minus a vote from a comment
def comment_minus_vote(request, post_id, comment_id):
    comment = Comment.objects.filter(post_id = post_id, id=comment_id)
    user = comment[0].user_id
    profile = RedditProfile.objects.filter(user_id = user.id)
    profile.update(karma=F('karma') + 1)
    comment.update(votes=F('votes') + 1)
    updated_comment = serializers.serialize('json', comment)
    return HttpResponse(updated_comment, content_type='json')

####### USER VIEWS #######
def user_profile(request, username):
    user = User.objects.get(username = username)
    user_profile = RedditProfile.objects.filter(user_id = user.id).values()
    profile_json = post = list(user_profile) 
    return JsonResponse(profile_json, safe=False)

def user_posts (request, username):
    user = User.objects.get(username = username)
    posts = serializers.serialize('json', TextPost.objects.filter(user_id = user.id))
    return HttpResponse(posts, content_type='json')