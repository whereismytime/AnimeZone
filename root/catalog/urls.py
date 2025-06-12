from django.urls import path
from .views import categories_view

app_name = 'catalog'
urlpatterns = [
    path('', categories_view, name='categories'),  # /catalog/
]
