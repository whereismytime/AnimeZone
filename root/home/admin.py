from django.contrib import admin
from .models import FeaturedAnime

@admin.register(FeaturedAnime)
class FeaturedAnimeAdmin(admin.ModelAdmin):
    list_display = ('anime', 'label', 'order')
    list_editable = ('order',)