from django.contrib import admin
<<<<<<< HEAD
from .models import FeaturedAnime

@admin.register(FeaturedAnime)
class FeaturedAnimeAdmin(admin.ModelAdmin):
    list_display = ('anime', 'label', 'order')
    list_editable = ('order',)
=======

# Register your models here.
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
