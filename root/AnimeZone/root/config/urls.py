from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
from home import views as home_views
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',      include(('home.urls',    'home'),    namespace='home')),
    path('catalog/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('blog/',   include(('blog.urls',   'blog'),    namespace='blog')),
    path('news/',   include(('news.urls',   'news'),    namespace='news')),
    path('accounts/', include(('accounts.urls','accounts'), namespace='accounts')),
    path('contact/', include(('contact.urls', 'contact'))),
]

=======
    
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
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
