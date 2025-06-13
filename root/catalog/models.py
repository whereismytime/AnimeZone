from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"

    def __str__(self):
        return self.name

class Anime(models.Model):
    CATEGORY_CHOICES = [
        ('live', 'Live Action'),
        ('trending', 'Trending Now'),
        ('popular', 'Popular Shows'),
        ('recent', 'Recently Added Shows'),
    ]

    title = models.CharField("Назва", max_length=200)
    slug = models.SlugField("Слаг", unique=True)
    image = models.ImageField("Обкладинка", upload_to='anime/%Y/%m/%d/')
    episodes = models.PositiveIntegerField("Кількість епізодів")
    genres = models.ManyToManyField(Genre, verbose_name="Жанри")
    rating = models.DecimalField("Рейтинг", max_digits=3, decimal_places=1)
    views = models.PositiveIntegerField("Перегляди", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField("Дата виходу", null=True, blank=True)

    category = models.CharField(
        "Категорія для головної",
        max_length=20,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True,
        help_text="Категорія для секцій головної сторінки"
    )

    class Meta:
        verbose_name = "Аніме"
        verbose_name_plural = "Аніме"

    def __str__(self):
        return self.title