from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('post/<slug:slug>/', views.blog_details, name='blog_details'),
]