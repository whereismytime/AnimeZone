from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # домашка
    path('', home_views.index, name='index'),
    path('anime-details/<slug:slug>/', home_views.anime_details, name='anime_details'),
    path('anime-watching/', home_views.anime_watching, name='anime_watching'),
    path('blog-details/', home_views.blog_details, name='blog_details'),
    
    # blog
    path('blog/', include('blog.urls')),

    # catalog app
    path('', include('catalog.urls')),

    # auth
    path('accounts/', include('accounts.urls')),
]

# 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
