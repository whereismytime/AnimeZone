from django.contrib import admin
<<<<<<< HEAD
from .models import Anime, Genre
from django.utils.html import format_html


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'episodes', 'rating', 'views', 'release_date', 'category', 'preview_image')
    list_filter = ('genres', 'release_date', 'category')  
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('genres',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 80px; border-radius: 4px;" />', obj.image.url)
        return "-"
    preview_image.short_description = "Обкладинка"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
=======

# Register your models here.
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
