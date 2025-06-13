from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify  # For slug generation
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.filter(status='published')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def blog_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    context = {
        'post': post
    }
    return render(request, 'blog/blog_details.html', context)

# Function to add blog posts
def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            
            # Assign author if authenticated
            if request.user.is_authenticated:
                new_post.author = request.user
            else:
                new_post.author = None

            # Generate unique slug for the post
            base_slug = slugify(new_post.title)
            unique_slug = base_slug
            num = 1
            while BlogPost.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{num}'
                num += 1
            new_post.slug = unique_slug

            new_post.save()

            return redirect('blog:blog_list')
    else:
        form = BlogPostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/add_post.html', context)
