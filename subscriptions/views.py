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


class SubscriberView(ListView):
    model = Subscription
    template_name = "subscriber.html"
    context_object_name = "followers"
    
    def get_queryset(self):
        return Subscription.objects.filter(to_user_id=self.kwargs['user_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        user = self.request.user
        to_user = get_object_or_404(User, pk=self.kwargs['user_id'])
        context['to_user'] = to_user
        following = Subscription.objects.filter(subscriber=to_user)
        followers = Subscription.objects.filter(to_user = to_user)
        context['following'] = following
        following_ids = Subscription.objects.filter(subscriber=user).values_list('to_user_id', flat=True)
        #print(list(Subscription.objects.filter(subscriber=to_user).values_list('to_user_id', flat=True)), list(Subscription.objects.filter(to_user = to_user).values_list('subscriber_id', flat=True)))
        context['following_ids'] = following_ids
        return context

class SubscriptionView(ListView):
    model = Subscription
    template_name = 'subscription.html'
    context_object_name = 'followings'

    def get_queryset(self):
        return Subscription.objects.filter(subscriber_id=self.kwargs['user_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        user = self.request.user
        to_user = get_object_or_404(User, pk=self.kwargs['user_id'])
        context['to_user'] = to_user
        followers = Subscription.objects.filter(to_user=to_user)
        context['followers'] = followers
        following_ids = Subscription.objects.filter(subscriber=user).values_list('to_user_id', flat=True)
        context['following_ids'] = following_ids
        return context
    
@login_required
def subscribe(request, user_id):
    subscriber = request.user
    to_user = get_object_or_404(get_user_model(), pk=user_id)
    subscription = Subscription.objects.filter(subscriber=subscriber, to_user=to_user).first()

    if subscription:
        subscription.delete()
    else:
        Subscription.objects.create(subscriber=subscriber, to_user=to_user)
    
    return redirect('users:user_profile', user_id=user_id)
    

    
