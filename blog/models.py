from turtle import title
from django.db import models
from django.db.models.fields import CharField, SlugField
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

#category
class Category(models.Model):
    name            = models.CharField(max_length=250)
    slug            = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering            = ('name', )
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("list_of_post_by_category", kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.name

#post
class Post(models.Model):
    STATUS_CHOICES  = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    title           = models.CharField(max_length=250)
    slug            = models.SlugField(max_length=250, unique=True)
    content         = models.TextField()
    seo_title       = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=160)
    author          = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    published       = models.DateTimeField(default=timezone.now)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    status          = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

class Navbar(models.Model):
    title = models.CharField(max_length=100)
    pageLink = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class main_menu(models.Model):
    m_menu_id = models.AutoField(primary_key=True)
    m_menu_name = models.CharField(max_length=50)
    m_menu_link = models.CharField(max_length=100)

#comment
'''class Comment(models.Model):
    post        = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user        = models.CharField(max_length=250)
    email       = models.EmailField()
    body        = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    approved    = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user'''