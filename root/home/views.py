<<<<<<< HEAD
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
=======
from django.shortcuts import render
from django.templatetags.static import static  # нужно для image_url

# Заглушки для товаров
DUMMY_PRODUCTS = [
    {
        'title': 'Naruto Shippuden',
        'image': 'img/trending/trend-1.jpg',
        'episodes': 500,
        'genres': ['Action', 'Adventure'],
        'rating': '9.0',
        'slug': 'naruto-shippuden',
        'views': 9141,
        'filter_classes': 'day years',
    },
    {
        'title': 'Attack on Titan',
        'image': 'img/trending/trend-2.jpg',
        'episodes': 87,
        'genres': ['Action', 'Drama'],
        'rating': '9.5',
        'slug': 'attack-on-titan',
        'views': 9141,
        'filter_classes': 'month week',
    },
    {
        'title': 'Demon Slayer',
        'image': 'img/trending/trend-3.jpg',
        'episodes': 26,
        'genres': ['Action', 'Fantasy'],
        'rating': '8.7',
        'slug': 'demon-slayer',
        'views': 9141,
        'filter_classes': 'week years',
    },
    {
        'title': 'Fate/stay night: Unlimited Blade Works',
        'image': 'img/trending/trend-4.jpg',
        'episodes': 26,
        'genres': ['Fantasy', 'Magic'],
        'rating': '8.4',
        'slug': 'fate-stay-night',
        'views': 8191,
        'filter_classes': 'day',
    },
    {
        'title': 'Gintama: The Final Movie',
        'image': 'img/trending/trend-5.jpg',
        'episodes': 1,
        'genres': ['Comedy', 'Action'],
        'rating': '9.1',
        'slug': 'gintama-final',
        'views': 7002,
        'filter_classes': 'week',
    },
    {
        'title': 'Fullmetal Alchemist: Brotherhood',
        'image': 'img/trending/trend-6.jpg',
        'episodes': 64,
        'genres': ['Action', 'Drama'],
        'rating': '9.2',
        'slug': 'fullmetal-alchemist',
        'views': 9999,
        'filter_classes': 'years',
    },
    {
        'title': 'Code Geass R2',
        'image': 'img/popular/popular-1.jpg',
        'episodes': 25,
        'genres': ['Mecha', 'Drama'],
        'rating': '8.9',
        'slug': 'code-geass-r2',
        'views': 8500,
        'filter_classes': 'month',
    },
    {
        'title': 'Sword Art Online',
        'image': 'img/popular/popular-2.jpg',
        'episodes': 25,
        'genres': ['Action', 'Game'],
        'rating': '7.5',
        'slug': 'sword-art-online',
        'views': 7400,
        'filter_classes': 'day week',
    },
    {
        'title': 'Haikyuu!!',
        'image': 'img/popular/popular-3.jpg',
        'episodes': 85,
        'genres': ['Sports', 'School'],
        'rating': '8.3',
        'slug': 'haikyuu',
        'views': 6630,
        'filter_classes': 'week month',
    },
    {
        'title': 'Boruto: Next Generations',
        'image': 'img/sidebar/tv-1.jpg',
        'episodes': 200,
        'genres': ['Action', 'Adventure'],
        'rating': '6.7',
        'slug': 'boruto',
        'views': 5500,
        'filter_classes': 'day',
    },
    {
        'title': 'Fate/Zero',
        'image': 'img/sidebar/tv-4.jpg',
        'episodes': 25,
        'genres': ['Action', 'Supernatural'],
        'rating': '8.6',
        'slug': 'fate-zero',
        'views': 4800,
        'filter_classes': 'years',
    },
    {
        'title': 'Mushishi',
        'image': 'img/live/live-3.jpg',
        'episodes': 20,
        'genres': ['Supernatural', 'Drama'],
        'rating': '8.4',
        'slug': 'mushishi',
        'views': 5200,
        'filter_classes': 'month',
    },
    {
        'title': 'Monogatari Series',
        'image': 'img/sidebar/comment-4.jpg',
        'episodes': 100,
        'genres': ['Mystery', 'Dialogue'],
        'rating': '8.8',
        'slug': 'monogatari-series',
        'views': 6300,
        'filter_classes': 'week',
    },
]



def index(request):
    context = {
        'trending_products': DUMMY_PRODUCTS[:6],
        'popular_products': DUMMY_PRODUCTS[6:9],
        'recent_products': DUMMY_PRODUCTS[9:12],
        'live_products': DUMMY_PRODUCTS[11:],
        'sidebar_products': DUMMY_PRODUCTS,
    }

    return render(request, 'anime/index.html', context)

def categories_view(request):
    genre = request.GET.get('genre')
    products = DUMMY_PRODUCTS

    if genre:
        products = [p for p in products if genre in p.get('genres', [])]

    context = {
        'products': products,
        'selected_genre': genre or "All",
        'all_genres': sorted({g for p in DUMMY_PRODUCTS for g in p['genres']}),
        'popular_products': DUMMY_PRODUCTS[6:11],  # ⬅️ вот это обязательно
    }
    return render(request, 'catalog/categories.html', context)


def anime_details(request, slug):
    anime = next((a for a in DUMMY_PRODUCTS if a['slug'] == slug), None)
    if not anime:
        return render(request, 'anime/404.html', status=404)
    return render(request, 'anime/anime-details.html', {'anime': anime})

def anime_watching(request):
    return render(request, 'anime/anime-watching.html')

def blog(request):
    return render(request, 'anime/blog.html')

def blog_details(request):
    return render(request, 'anime/blog-details.html')

def login_view(request):
    return render(request, 'anime/login.html')

def signup(request):
    return render(request, 'anime/signup.html')
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
