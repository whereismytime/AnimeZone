from django.db import models
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Tag(models.Model):
    name = models.CharField("Назва тега", max_length=50, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    slug = models.SlugField("Слаг", unique=True, max_length=200)
    content = models.TextField("Вміст")
    published_at = models.DateTimeField("Дата публікації", default=timezone.now)  
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    image = models.ImageField("Зображення (фон)", upload_to="news/", null=True, blank=True)
    is_featured = models.BooleanField("Виділити як нову", default=False)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def is_recent(self):
        return self.is_featured  
=======

# Create your models here.
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
