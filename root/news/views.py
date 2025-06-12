<<<<<<< HEAD
from django.shortcuts import render
from .models import NewsArticle

def news(request):
    articles = NewsArticle.objects.order_by('-published_at')
    return render(request, 'news/news_list.html', {'articles': articles})
=======
from django.http import HttpResponse

def news(request):
    return HttpResponse("News page")
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
