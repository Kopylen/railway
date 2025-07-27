from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from homee.views import HomePage, ShowPost, Tags, AddPage, DeletePage, TemplateView
from category.views import Category
from popular.views import popular
from logr.views import *

app_name = 'users'



urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('register/done/', register_done, name='register_done'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('setting/', SettingUser, name='setting'),
    path('password-change/', UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done', 
         PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password-reset/', 
         PasswordResetView.as_view(template_name='password_reset_form.html', 
                                   email_template_name='password_reset_email.html', 
                                   success_url=reverse_lazy('users:password_reset_done')), 
                                   name='password_reset'),
    path('password-reset/done/', 
         PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html',
             success_url=reverse_lazy('users:password_reset_complete')), 
             name='password_reset_confirm'),
    path('password-reset/complete',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),  
    path('edit/<int:post_id>/', UpdatePage.as_view(), name='edit_post'),
    path('userprofile/<int:user_id>/', UserProfile.as_view(), name='user_profile')
]



#source env/bin/activate  