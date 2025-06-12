from django.urls import path
from . import views

<<<<<<< HEAD
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<slug:slug>/', views.anime_details, name='anime_details'),
=======
urlpatterns = [
    path('', views.home, name='home'),
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
]
