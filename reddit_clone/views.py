from django.shortcuts import render
from .models import TextPost, Comment, RedditProfile, SubReddit
from django.http import JsonResponse, HttpResponse
from urllib import parse
# from django.contrib.auth.models import User
import json

####### FRONT PAGE #######
def all_posts(request):
    posts = TextPost.objects.all()
    results = [post.to_json() for post in posts]

    return HttpResponse(json.dumps(results), content_type="application/json")

####### POSTS VIEWS #######
# GET all posts from subreddit
def all_posts_from(request, slug):
    subreddit = SubReddit.objects.get(slug=slug)
    posts = TextPost.objects.filter(subreddit_id=subreddit)
    results = [post.to_json() for post in posts]

    return HttpResponse(json.dumps(results), content_type="application/json")

# GET one post by id
def post_detail(request, pk):
    post = TextPost.objects.filter(id=pk).values()
    post = list(post) 
    return JsonResponse(post, safe=False)

# POST add a vote to a post
def post_upvote(request, pk):
    post = TextPost.objects.get(id=pk)
    # user = post.user_id
    # profile = RedditProfile.objects.get(user_id = user.id)
    # profile.vote(1)
    post.vote(1)
    # profile.save()
    post.save()
    results = [post.to_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")


# POST minus a vote to a post
def post_downvote(request, pk):
    post = TextPost.objects.get(id=pk)
    # user = post.user_id
    # profile = RedditProfile.objects.get(user_id = user.id)
    # profile.vote(-1)
    post.vote-(1)
    # profile.save()
    post.save()
    results = [post.to_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")

# POST add a post to the database
def add_post(request):
    
    print('received: ')
    print(request.GET.urlencode())
    query = request.GET.urlencode()
    newPost = parse.parse_qs(query)
    print(newPost.get('tag_line')[0])
    savedPost = TextPost.objects.create(tag_line=newPost['tag_line'][0], content=newPost.get('content')[0], votes=newPost.get('votes')[0], thumbnail_image_url=newPost.get('thumbnail_image_url')[0])
    savedPost.save()
    results = [savedPost.to_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")

####### COMMENT VIEWS ########
# GET all comments on a post
def post_comments(request, post_id):
    comments = Comment.objects.filter(post_id = post_id)
    results = [comment.to_json() for comment in comments]

    return HttpResponse(json.dumps(results), content_type="application/json")

#GET comment by id
def comment_detail(request, post_id, comment_id):
    comments = Comment.objects.filter(post_id = post_id, id=comment_id)
    results = [comment.to_json() for comment in comments]

    return HttpResponse(json.dumps(results), content_type="application/json")

#POST add a vote to a comment
def comment_upvote(request, post_id, comment_id):
    comment = Comment.objects.get(post_id = post_id, id=comment_id)
    # user = comment.user_id
    # profile = RedditProfile.objects.get(user_id = user.id)
    profile.vote(1)
    comment.vote(1)
    profile.save()
    comment.save()
    results = [comment.to_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")

#POST minus a vote from a comment
def comment_downvote(request, post_id, comment_id):
    comment = Comment.objects.get(post_id = post_id, id=comment_id)
    # user = comment.user_id
    # profile = RedditProfile.objects.get(user_id = user.id)
    # profile.vote(-1)
    comment.vote(-1)
    # profile.save()
    comment.save()
    results = [comment.to_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")

####### USER VIEWS #######
# def user_profile(request, username):
#     user = User.objects.get(username = username)
#     profile = RedditProfile.objects.get(user_id = user)
#     results = [profile.to_json()]
#     return HttpResponse(json.dumps(results), content_type="application/json")


# def user_posts (request, username):
#     ##
#     user = User.objects.get(username = username)
#     posts = TextPost.objects.filter(user_id = user)
#     results = [post.to_json() for post in posts]

#     return HttpResponse(json.dumps(results), content_type="application/json")

####### SUBREDDIT VIEWS #######
def all_subreddits(request):
    subreddits = SubReddit.objects.all()
    results = [subreddit.to_json() for subreddit in subreddits]

    return HttpResponse(json.dumps(results), content_type="application/json")
