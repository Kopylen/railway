from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms, template
from django.urls import reverse, reverse_lazy
from subscriptions.models import Subscription
from myproject.datas import data_db
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

class UserView(ListView):
    model = get_user_model()
    template_name = 'users.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        following_ids = Subscription.objects.filter(subscriber=user).values_list('to_user_id', flat=True)
        context['following_ids'] = following_ids

        return context