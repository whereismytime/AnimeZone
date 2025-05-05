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
    }
    return render(request, 'catalog/categories.html', context)
