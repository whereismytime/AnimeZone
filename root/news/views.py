from django.shortcuts import render
from .models import NewsArticle

def news(request):
    articles = NewsArticle.objects.order_by('-published_at')
    return render(request, 'news/news_list.html', {'articles': articles})
