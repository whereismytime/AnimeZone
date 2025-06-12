from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',      include(('home.urls',    'home'),    namespace='home')),
    path('catalog/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('blog/',   include(('blog.urls',   'blog'),    namespace='blog')),
    path('news/',   include(('news.urls',   'news'),    namespace='news')),
    path('accounts/', include(('accounts.urls','accounts'), namespace='accounts')),
    path('contact/', include(('contact.urls', 'contact'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
