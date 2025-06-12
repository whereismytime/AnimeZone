from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<slug:slug>/', views.anime_details, name='anime_details'),
]
