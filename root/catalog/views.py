<<<<<<< HEAD
from django.shortcuts import render
from django.utils import timezone
from catalog.models import Anime, Genre
from utils.time_class import get_main_time_class

def categories_view(request):
    genre_name = request.GET.get('genre')
    now = timezone.now()

    if genre_name and genre_name != "All":
        products_qs = Anime.objects.filter(genres__name=genre_name).distinct()
    else:
        products_qs = Anime.objects.all()

    for anime in products_qs:
        anime.filter_class = get_main_time_class(now - anime.created_at)

    top_views = Anime.objects.order_by('-views')[:7]  

    context = {
        'products': products_qs,
        'selected_genre': genre_name or "All",
        'all_genres': Genre.objects.order_by('name'),
        'top_views': top_views,
        'selected_period': 'day',
=======
# catalog/views.py
from django.shortcuts import render
from home.views import DUMMY_PRODUCTS 

def categories_view(request):
    genre = request.GET.get('genre')
    products = DUMMY_PRODUCTS

    if genre:
        products = [p for p in products if genre in p.get('genres', [])]

    context = {
        'products': products,
        'selected_genre': genre or "All",
        'all_genres': sorted({g for p in DUMMY_PRODUCTS for g in p['genres']}),
        'popular_products': DUMMY_PRODUCTS[:5],  
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
    }
    return render(request, 'catalog/categories.html', context)
