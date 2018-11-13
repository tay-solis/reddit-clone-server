from django.urls import path
from . import views

urlpatterns = [
# All Post Paths
    path('post/all', views.all_posts, name='all_posts'),
    path('r/<slug>/post/all', views.all_posts_from, name='all_posts_from'),
# Individual Post Paths
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/upvote', views.post_upvote, name='post_upvote'),
    path('post/<int:pk>/downvote', views.post_downvote, name='post_downvote'),
# Comments Paths
    path('post/<int:post_id>/comments', views.post_comments, name='post_comments'),
    path('post/<int:post_id>/comments/<int:comment_id>', views.comment_detail, name='comment_detail'),
    path('post/<int:post_id>/comments/<int:comment_id>/upvote', views.comment_upvote, name='comment_upvote'),
    path('post/<int:post_id>/comments/<int:comment_id>/downvote', views.comment_downvote, name='comment_downvote'),
# User Paths
    path('u/<username>', views.user_profile, name='user_profile'),
    path('u/<username>/post/all', views.user_posts, name='user_posts'),
]