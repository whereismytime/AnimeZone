from django.urls import path
from . import views

<<<<<<< HEAD
app_name = 'news'
=======
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
urlpatterns = [
    path('', views.news, name='news'),
]
