from django.db import models
<<<<<<< HEAD
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
=======

# Create your models here.
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
