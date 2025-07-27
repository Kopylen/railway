from django import forms
from .models import *
from .models import TagPost, TagPost2
from django.core.exceptions import ValidationError

class AddPost(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Category', empty_label="Doesn't choosen   ")

    class Meta:
        model = Home
        fields = ['title', 'photo', 'about', 'post', 'is_published', 'cat', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            #'slug': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            #'author': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'about': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 5}),
            'post': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 6}),
            'tags': forms.SelectMultiple(attrs={'class': 'w-full border border-gray-500 rounded'})
        }
        labels = {
            'slug': 'URL',
        }


class UpdatePost(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Category', empty_label="Doesn't choosen")

    class Meta:
        model = Home
        fields = ['title', 'photo', 'about', 'post', 'is_published', 'cat', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            #'author': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'about': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 5}),
            'post': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 6}),
            'tags': forms.SelectMultiple(attrs={'class': 'w-full border border-gray-500 rounded'}),
        }


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')




class ReplyCreatForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded text-sm resize-none focus:outline-none focus:ring-1 focus:ring-blue-400',
                'rows': 2,
                'placeholder': 'Write a reply...'
            })
        }
        labels = {
            'body': ''
        }