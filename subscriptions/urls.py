from django.contrib import admin
from django.urls import path, include
import subscriptions.views

from subscriptions.views import *

urlpatterns = [
    path('subscribers/<int:user_id>/', SubscriberView.as_view(), name='subscriber'),
    path('subscriptions/<int:user_id>/', SubscriptionView.as_view(), name='subscription'),
    path('subscribe/<int:user_id>/', subscribe, name='subscribe'),
]