from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms, template
from django.urls import reverse, reverse_lazy
from homee.forms import UpdatePost
from homee.models import Home
from myproject.datas import data_db
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, UpdateView, View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from subscriptions.models import *


from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm, EditPostForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'log.html'
    extra_context = {'title': 'Login'}
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:register_done')

def register_done(request):
    return render(request, 'register_done.html')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile.html'
    context_object_name = 'data'

    extra_context = {
        'user_photo': '/media/users/default.png',
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')
    
    def get_object(self, queryset = None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Home.objects.filter(author=user)
        followers = Subscription.objects.filter(to_user = user).count()
        followings = Subscription.objects.filter(subscriber = user).count()
        context['followers'] = followers
        context['followings'] = followings
        return context

class UserProfile(DetailView):
    model = get_user_model()
    template_name = 'user_profile.html'
    context_object_name = 'data'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Home.objects.filter(author=user)
        followers = Subscription.objects.filter(to_user = user)
        followings = Subscription.objects.filter(subscriber = user)
        context['followers'] = followers
        context['followings'] = followings
        context['follower_ids'] = followers.values_list('subscriber__id', flat=True)
        return context

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')


@login_required
def SettingUser(request):
    posts = ''
    is_superuser = False
    #print(str(request.user))
    if str(request.user) == 'Kudaiberdi':
        posts = Home.objects.all()
        is_superuser = True
    else:
        posts = Home.objects.filter(author=request.user)
    
    extra_context = {
        'posts': posts,
        'is_superuser': is_superuser,
    }
    return render(request, 'settings.html', context=extra_context)


class UpdatePage(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Home
    form_class = UpdatePost
    template_name = 'edit_post.html'
    success_url = reverse_lazy('users:setting')
    title_page = 'Update Post.'
    pk_url_kwarg = 'post_id'
    permission_required = 'homee.change_home'

    def get_object(self, queryset=None):
        return get_object_or_404(Home, id=self.kwargs[self.pk_url_kwarg])