from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Чорнетка'),
        ('published', 'Опубліковано'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
