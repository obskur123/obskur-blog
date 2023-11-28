from django.urls import path
from .views import sign_in, create_post, post, sign_out, add_comment, comments, home, posts, delete_post, delete_comment, toggle_archived


urlpatterns = [
    path('home/', home, name='home'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
    path('post/all', posts, name='posts'),
    path('post/edit/toggle-archived/<int:post_id>', toggle_archived, name='toggle-archived'), 
    path('post/create', create_post, name='create-post'),
    path('post/delete/<int:post_id>', delete_post, name='delete-post'),
    path('post/get/<int:post_id>', post, name='post'),
    path('comment/all/<int:post_id>', comments, name='comments'),
    path('comment/delete/<int:comment_id>', delete_comment, name='delete-comment'),
    path('comment/create/<int:post_id>', add_comment, name='add-comment'),
]
