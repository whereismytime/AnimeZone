from django.shortcuts import render, get_object_or_404
from catalog.models import Anime
from home.models import FeaturedAnime
from utils.helpers import add_filter_class_to_queryset

def index(request):
    """
    Представление для главной страницы.
    """
    all_anime_qs = Anime.objects.all()

    all_anime_with_class = add_filter_class_to_queryset(all_anime_qs)

    trending_products = [a for a in all_anime_with_class if a.category == 'trending'][:6]
    popular_products = [a for a in all_anime_with_class if a.category == 'popular'][:6]
    recent_products = [a for a in all_anime_with_class if a.category == 'recent'][:6]
    live_products = [a for a in all_anime_with_class if a.category == 'live'][:6]

    top_views = Anime.objects.order_by('-views')[:7]

    context = {
        'featured_anime': FeaturedAnime.objects.select_related('anime').order_by('order'),
        'trending_products': trending_products,
        'popular_products': popular_products,
        'recent_products': recent_products,
        'live_products': live_products,
        'top_views': top_views,
    }
    return render(request, 'anime/index.html', context)

def anime_details(request, slug):
    """
    Представление для страницы с детальной информацией об аниме.
    """
    anime = get_object_or_404(Anime, slug=slug)
    return render(request, 'anime/anime-details.html', {'anime': anime})

def anime_watching(request, slug):
    """
    Представление для страницы просмотра аниме.
    """
    anime = get_object_or_404(Anime, slug=slug)
    
    context = {
        'anime': anime,
    }
    return render(request, 'anime/anime-watching.html', context)