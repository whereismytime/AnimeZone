# accounts/middleware.py

from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.contrib import messages

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.protected_url_names = [
            'blog:add_blog_post', 
            'accounts:profile'
        ]

    def __call__(self, request):
        if request.path_info == reverse('accounts:login'):
            return self.get_response(request)

        if request.path.startswith(reverse('admin:index')) and not request.user.is_staff:
            messages.warning(request, 'You do not have permission to access this page.')
            return redirect('index')

        try:
            resolver_match = resolve(request.path_info)
            current_url_name = f"{resolver_match.namespace}:{resolver_match.url_name}"
            
            if current_url_name in self.protected_url_names and not request.user.is_authenticated:
                messages.warning(request, 'You need to log in to access this page.')
                login_url = f"{reverse('accounts:login')}?next={request.path}"
                return redirect(login_url)
        except:
            pass

        response = self.get_response(request)
        return response