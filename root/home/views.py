from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from catalog.models import Anime, Genre
from home.models import FeaturedAnime
from utils.time_class import get_main_time_class

def index(request):
    now = timezone.now()
    all_anime = Anime.objects.all()

    for anime in all_anime:
        anime.filter_class = get_main_time_class(now - anime.created_at)

    context = {
        'featured_anime': FeaturedAnime.objects.select_related('anime').order_by('order'),
        'trending_products': all_anime.filter(category='trending')[:6],
        'popular_products': all_anime.filter(category='popular')[:6],
        'recent_products': all_anime.filter(category='recent')[:6],
        'live_products': all_anime.filter(category='live')[:6],
        'top_views': Anime.objects.all().order_by('-views')[:7],  
    }
    return render(request, 'anime/index.html', context)




def anime_details(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    return render(request, 'anime/anime-details.html', {'anime': anime})


def categories_view(request):
    genre_name = request.GET.get('genre')
    now = timezone.now()

    products_qs = (
        Anime.objects.filter(genres__name=genre_name).distinct()
        if genre_name else
        Anime.objects.all()
    )

    for anime in products_qs:
        anime.filter_class = get_main_time_class(now - anime.created_at)


    popular_qs = Anime.objects.order_by('-views')[:20]
    for anime in popular_qs:
        anime.filter_class = get_main_time_class(now - anime.created_at)

    context = {
        'products': products_qs,
        'selected_genre': genre_name or "All",
        'all_genres': Genre.objects.order_by('name'),
        'popular_products': popular_qs,
        'selected_period': 'day',
    }
    return render(request, 'catalog/categories.html', context)
