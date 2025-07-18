from django import forms
from .models import Categories as Category, Home
from .models import TagPost
from django.core.exceptions import ValidationError

class AddPost(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label="Doesn't choosen   ")

    class Meta:
        model = Home
        fields = ['title', 'slug', 'photo', 'author', 'about', 'post', 'is_published', 'cat', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'slug': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'author': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'about': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 5}),
            'post': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 6}),
            'tags': forms.SelectMultiple(attrs={'class': 'w-full border border-gray-500 rounded'})
        }
        labels = {
            'slug': 'URL',
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title)>50:
    #         raise forms.ValidationError("Title must be less than 50 characters.")
        
    #     return title



class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')





    # title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    # slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}), label='URL')
    # author = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    # about = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 5}))
    # post = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded', 'rows': 6}))
    # is_published = forms.BooleanField(required=False)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label="Doesn't choosen   ")
    # #tag = forms.ModelChoiceField(queryset=TagPost.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'w-full border border-gray-500 rounded'}), label='Tags')
