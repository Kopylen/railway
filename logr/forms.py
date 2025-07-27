from homee.models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Log in', 
                               widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    password = forms.CharField(max_length=100, label='Password', 
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Log in', 
                               widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    password1 = forms.CharField(max_length=100, label='Password', 
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    password2 = forms.CharField(max_length=100, label='Confirm Password', 
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    

    class Meta:
        model = get_user_model() 
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
             'email': 'E-mail',
             'first_name': 'Firs Name',
             'last_name': 'Last Name'
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
        }

        def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model().objects.filter(email='email').exists:
                raise forms.ValidationError("This email is already taken")
            return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Log in', 
                               widget=forms.TextInput(attrs={
                                   'class': 'w-full px-4 py-2 border border-gray-500 rounded bg-gray-100 cursor-not-allowed',
                                   'readonly': 'readonly'
                               }))

    class Meta:
        model = get_user_model() 
        fields = ['photo', 'username', 'email', 'first_name', 'last_name']
        labels = {
             'email': 'E-mail',
             'first_name': 'Firs Name',
             'last_name': 'Last Name'
        }

        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-500 rounded bg-gray-100 cursor-not-allowed',
                'readonly': 'readonly'
            }),
            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', 
                                   widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    new_password1 = forms.CharField(max_length=100, label='New Password', 
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    new_password2 = forms.CharField(max_length=100, label='Confirm Password', 
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}))
    


# Form for editing posts
class EditPostForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = ['title', 'photo', 'about', 'post', 'is_published', 'cat', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'about': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'post': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'cat': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
            'tags': forms.SelectMultiple(attrs={'class': 'w-full px-4 py-2 border border-gray-500 rounded'}),
        }

