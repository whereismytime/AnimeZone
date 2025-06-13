from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class AuthRequiredMiddleware:
    """
    Middleware для захисту певних URL від неавторизованих користувачів
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # URL які потребують авторизації
        self.protected_urls = [
            '/blog/add/',
            '/profile/',
            '/admin/',
        ]

    def __call__(self, request):
        # Перевіряємо чи URL потребує авторизації
        for url in self.protected_urls:
            if request.path.startswith(url) and not request.user.is_authenticated:
                messages.warning(request, 'Для доступу до цієї сторінки потрібно увійти в систему.')
                return redirect('accounts:login')

        response = self.get_response(request)
        return response