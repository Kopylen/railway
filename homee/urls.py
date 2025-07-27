from django.contrib import admin
from django.urls import path, include

from homee.views import *
from homee.views import delete_reply
from category.views import Category
from popular.views import popular
from users.views import *

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('popular/', popular, name='popular'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', Category.as_view(), name='cat'),
    path('tag/<slug:tag_slug>/', Tags.as_view(), name='tag'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comment/delete/<slug:comment_id>/', delete_comment, name='delete_comment'),
    path('comment/<slug:comment_id>/reply/', add_reply, name='add_reply'),
    path('reply/delete/<slug:reply_id>/', delete_reply, name='delete_reply'),
    
    path('addpost/', AddPage.as_view(), name='add_post'),
    path('delete/<int:pk>/', DeletePage.as_view(), name='delete'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('users/', UserView.as_view(), name='users')
]


#source env/bin/activate  