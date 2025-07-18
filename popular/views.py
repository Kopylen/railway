from django.shortcuts import render
from django.http import HttpResponse
from django import template
from homee.models import Home
from myproject.datas import data_db


def popular(request):

    db = Home.published.all().order_by('-likes')

    t = {"main_title": "Crafty Tips",
         'post': db,
    }

    return render(request, "popular.html", context = t)
