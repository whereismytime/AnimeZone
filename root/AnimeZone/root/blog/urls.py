from django.urls import path
<<<<<<< HEAD
from . import views

app_name = 'blog'
urlpatterns = [
    path('',      views.blog_list,     name='blog_list'),
    path('add/',  views.add_blog_post, name='add_blog_post'),
    path('<slug:slug>/', views.blog_details, name='blog_details'),
]
=======
from . import views 

app_name = 'blog' 

urlpatterns = [
    path('', views.blog_list, name='blog_list'), 
    path('add/', views.add_blog_post, name='add_blog_post'),\
    path('<slug:slug>/', views.blog_details, name='blog_details'), 
]
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
