from django.contrib import admin
from .models import NewsArticle, Tag
from django.utils.html import format_html
from django.utils.timezone import localtime

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author_label', 'formatted_date', 'is_new', 'image_preview')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published_at', 'is_featured', 'tags')
    filter_horizontal = ('tags',)

    def formatted_date(self, obj):
        return localtime(obj.published_at).strftime("%d.%m.%Y %H:%M")
    formatted_date.short_description = "Дата"

    def author_label(self, obj):
        if obj.author and obj.author.is_superuser:
            return format_html(
                '<strong style="color: #e53637;">{} <span style="font-size: 11px; background: #e53637; color: white; padding: 2px 5px; border-radius: 3px;">ADMIN</span></strong>',
                obj.author.username
            )
        elif obj.author:
            return obj.author.username
        return "-"
    author_label.short_description = "Автор"

    def is_new(self, obj):
        return "🆕" if obj.is_recent() else ""
    is_new.short_description = "NEW"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 60px; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Зображення"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
