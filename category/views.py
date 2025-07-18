from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import template
from homee.models import Home, TagPost
from homee.models import Categories
from myproject.datas import data_db


def categories(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Home.published.filter(cat_id=category.pk)

    cnt=posts.exists()

    data = {
        'title': category.name,
        'post': posts,
        'count': cnt
    }

    return render(request, "cat_post.html", context = data)
