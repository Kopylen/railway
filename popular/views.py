from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.db.models import Count
from homee.models import Home
from myproject.datas import data_db
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView


def popular(request):
     db = Home.published.annotate(likes_count=Count('likes')).order_by('-likes_count')

     t = {"main_title": "Crafty Tips",
          'post': db,
     }

     return render(request, "popular.html", context = t)
