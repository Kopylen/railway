import uuid
from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Home.Status.PUBLISHED)

class Home(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Drafts'
        PUBLISHED = 1, 'Published'

    time = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="static/photos/%Y/%m/%d", default=None, blank=True, null=True, verbose_name='Image')
    status = models.CharField(max_length=255)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)
    about = models.TextField(blank=True)
    post = models.TextField(blank=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]) ,Status.choices)), 
                                       default=Status.DRAFT)

    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    tags2 = models.ManyToManyField('TagPost2', blank=True, related_name='posts2')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='author', null=True, default=None)

    objects = models.Manager()
    published = PublishedManager()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    def save(self, *args, **kwargs):
        if 1:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Home.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Content"
        ordering = ["-time_update"]
        indexes = [
            models.Index(fields=ordering)
        ]
    

class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

class TagPost(models.Model):
    tag = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
    
    class Meta:
        verbose_name = "Tag"        
        verbose_name_plural = "Tags"

class TagPost2(models.Model):
    tag = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse('tag2', kwargs={'tag_slug': self.slug})
    
    class Meta:
        verbose_name = "Tag2"        
        verbose_name_plural = "Tags2"

class UploadFiles(models.Model):
    file = models.FileField(upload_to='upload_model')

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'
        
    class Meta:
        ordering = ['-created']


class Reply(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'
        
    class Meta:
        ordering = ['created']