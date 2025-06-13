from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_views.index, name='index'),
    path('anime-details/<slug:slug>/', home_views.anime_details, name='anime_details'),
    path('anime-watching/<slug:slug>/', home_views.anime_watching, name='anime_watching'),

    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('catalog/', include('catalog.urls')),
    path('contact/', include('contact.urls')),
    path('news/', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)