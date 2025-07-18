from django.shortcuts import render
from django.http import HttpResponse
from django import template
from myproject.datas import data_db


def login(request):
    t = {"main_title": "Crafty Tips",
    }
    return render(request, 'log.html', t)


def register(request):
    t = {"main_title": "Crafty Tips",
    }
    return render(request, 'register.html', t)