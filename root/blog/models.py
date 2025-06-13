from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class BlogPost(models.Model):
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(unique=True, max_length=200, verbose_name="URL Slug (auto-generated if empty)")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Post Image", blank=True, null=True)
    
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts',
        verbose_name="Author"
    )
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name="Publication Status"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Publication Date")

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-published_at']

    def __str__(self):
        return self.title
