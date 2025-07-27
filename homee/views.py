from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django import template
from django.urls import reverse, reverse_lazy
from django.views import View
from homee.models import Home, TagPost, UploadFiles, TagPost2, Comment
from homee.utils import DataMixin
from myproject.datas import data_db
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
import os
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model




class HomePage(DataMixin, ListView):
    model=get_user_model()
    template_name = "index.html"
    context_object_name = 'post'
    title_page = "Latest Tips & Hacks"


    def get_queryset(self):
        return Home.published.all().order_by('-time_update').select_related('cat')

@require_POST
@login_required
def like_post(request, post_id):
    post = Home.objects.get(id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({
        'likes': post.likes.count(),
        'liked': liked,
    })

class ShowPost(DataMixin, DetailView):
    model = Home
    template_name = "post.html"
    context_object_name = 'data'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixed_context(context, title=context['data'].title)

    
    def get_object(self, queryset=None):
        return get_object_or_404(Home, id=self.kwargs[self.pk_url_kwarg])


class Tags(DataMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Home.published.filter(tags__slug=self.kwargs['tag_slug']).order_by('-time').select_related('cat')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tagg = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixed_context(context, title=f'Tag: {tagg.tag}')

    
class AddPage(PermissionRequiredMixin,  LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPost
    template_name = 'add_post.html'
    title_page = 'Add new Post.'
    permission_required = 'homee.add_home'
    extra_context = {'type': 'p'}

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

    
class DeletePage(PermissionRequiredMixin, DataMixin, DeleteView):
    model = Home
    success_url = reverse_lazy('home')
    template_name = 'add_post.html'
    title_page = 'Delete Post.'
    extra_context = {'type': 'd'}
    permission_required = 'homee.delete_home'

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        body = request.POST.get('body')
        post = get_object_or_404(Home, id=post_id)

        if body:
            Comment.objects.create(
                author=request.user,
                parent_post=post,
                body=body
            )

    return redirect('post', post_id=post.id)


@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.parent_post

    if request.method == 'POST':
        body = request.POST.get('reply_body')
        if body:
            Reply.objects.create(
                author=request.user,
                parent_comment=comment,
                body=body
            )

    return redirect('post', post_id=post.id)



def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
    return redirect('post', post_id=comment.parent_post.id)


# Delete a reply if the user is the author
from homee.models import Reply  # Ensure Reply is imported

@login_required
@require_POST
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if reply.author == request.user:
        reply.delete()
    return redirect('post', post_id=reply.parent_comment.parent_post.id)
