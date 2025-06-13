from django.db import models
from catalog.models import Anime

class FeaturedAnime(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='hero/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Герой-слайд"
        verbose_name_plural = "Герой-слайди"
        ordering = ['order']

    def __str__(self):
        return f"{self.label} — {self.anime.title}"
