from django.shortcuts import render
from .models import Anime, Genre
from utils.helpers import add_filter_class_to_queryset

def categories_view(request):
    """
    Представление для страницы категорий (каталога).
    """
    genre_name = request.GET.get('genre')

    if genre_name and genre_name != "All":
        products_qs = Anime.objects.filter(genres__name=genre_name).distinct()
    else:
        products_qs = Anime.objects.all()

    top_views_qs = Anime.objects.order_by('-views')[:7]

    products_with_class = add_filter_class_to_queryset(products_qs)
    top_views_with_class = add_filter_class_to_queryset(top_views_qs)

    context = {
        'products': products_with_class,
        'selected_genre': genre_name or "All",
        'all_genres': Genre.objects.order_by('name'),
        'top_views': top_views_with_class, 
        'selected_period': 'day',
    }
    return render(request, 'catalog/categories.html', context)