from django.contrib import admin
from django.urls import path, include

from homee.views import home, post, show_tags, add_post
from category.views import categories
from popular.views import popular
from logr.views import login, register

urlpatterns = [
    path('', home, name="home"),
    path('popular/', popular, name='popular'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('post/<slug:post_slug>/', post, name='post'),
    path('category/<slug:cat_slug>/', categories, name='cat'),
    path('tag/<slug:tag_slug>/', show_tags, name='tag'),
    path('addpost/', add_post, name='add_post'),
]


#source env/bin/activate  