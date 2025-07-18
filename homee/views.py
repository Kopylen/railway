from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django import template
from homee.models import Home, TagPost, UploadFiles
from myproject.datas import data_db
from .forms import AddPost
import os


def home(request):
    db=Home.published.all().order_by('-time').select_related('cat')
    t = {
        "main_title": "Crafty Tips",
        'title': "Latest Tips & Hacks",
         'post': db
    }

    return render(request, "index.html", context = t)

def post(request, post_slug):
    post=get_object_or_404(Home.published.all(), slug=post_slug)
    # db=sorted(data_db, key=lambda x: x['data'], reverse=True)
    # dp=[]
    # for i in db:
    #     if i['id']==post_id:
    #         dp.append(i)
    #         break
    t = {"main_title": "Crafty Tips",
         'data': post,
    }

    return render(request, "post.html", context = t)


def show_tags(reques, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=1)

    data = {
        "main_title": "Crafty Tips",
        'title': f'Tag: {tag.tag}',
        'post': posts,
    }

    return render(reques, 'index.html', context=data)

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            if 'file_upload' in request.FILES:
                #handle_uploaded_file(request.FILES['file_upload'])
                fp = UploadFiles(file=request.FILES['file_upload'])
                fp.save()
            form.save()
            return redirect('home')
    else:
        form = AddPost()
    return render(request, 'add_post.html', {'form': form})