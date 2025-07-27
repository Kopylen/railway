from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class User(AbstractUser):
    photo = models.ImageField(upload_to='static/users/%Y/%m/%d/', blank=True, null=True, verbose_name='Photo')
