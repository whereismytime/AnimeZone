from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})

def blog_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_details.html', {'post': post})