from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import template
from homee.models import Home, TagPost
from homee.models import Categories
from myproject.datas import data_db
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView


class Category(ListView):
    template_name = "cat_post.html"
    context_object_name = 'post'
    allow_empty = True

    def get_queryset(self):
        return Home.published.filter(cat__slug=self.kwargs['cat_slug'])
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        posts = contex['post']
        
        contex['main_title'] = "Crafty Tips"
        contex['count'] = len(posts)

        if posts:
            cat = posts[0].cat
            contex['title'] = 'Latest '+cat.name
        else:
            contex['title'] = "No posts in this category"

        return contex
