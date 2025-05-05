# catalog/urls.py
from django.urls import path
from .views import categories_view

urlpatterns = [
    path('categories/', categories_view, name='categories'),
]
