from django.utils.text import slugify
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Home.Status.PUBLISHED)

class Home(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Drafts'
        PUBLISHED = 1, 'Published'

    time = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", default=None, blank=True, null=True, verbose_name='Image')
    content = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, unique=False)
    status = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    about = models.TextField(blank=True)
    post = models.TextField(blank=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]) ,Status.choices)), 
                                       default=Status.DRAFT)

    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')


    objects = models.Manager()
    published = PublishedManager()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
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
        ordering = ["-time"]
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

class UploadFiles(models.Model):
    file = models.FileField(upload_to='upload_model')