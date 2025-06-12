<<<<<<< HEAD
from django.urls import path
from .views import categories_view

app_name = 'catalog'
urlpatterns = [
    path('', categories_view, name='categories'),  # /catalog/
=======
# catalog/urls.py
from django.urls import path
from .views import categories_view

urlpatterns = [
    path('categories/', categories_view, name='categories'),
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
]
