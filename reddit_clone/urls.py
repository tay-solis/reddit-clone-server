from django.urls import path
from . import views

urlpatterns = [
    path('post/all', views.all_posts, name='all_posts'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/addvote', views.post_add_vote, name='post_add_vote'),
    path('post/<int:pk>/minusvote', views.post_minus_vote, name='post_minus_vote'),
    path('post/<int:post_id>/comments', views.post_comments, name='post_comments'),
    path('post/<int:post_id>/comments/<int:comment_id>', views.comment_detail, name='comment_detail'),
    path('post/<int:post_id>/comments/<int:comment_id>/addvote', views.comment_add_vote, name='comment_add_vote'),
    path('post/<int:post_id>/comments/<int:comment_id>/minusvote', views.comment_minus_vote, name='comment_minus_vote'),
]