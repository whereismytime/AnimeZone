from django.db import models 
from django.contrib.auth.models import User 
from django.utils import timezone 
from django.urls import reverse 


class BlogPost(models.Model):
    
    STATUS_CHOICES = [
        ('draft', 'Чорнетка'),   
        ('published', 'Опубліковано'), 
    ]

    # --- ОСНОВНІ ПОЛЯ ПОСТА ---
    title = models.CharField(max_length=200, verbose_name="Заголовок") # verbose_name - це просто назва поля в адмінці.
    slug = models.SlugField(unique=True, max_length=200, verbose_name="URL-слаг (автоматично генерується, якщо пусто)") # Це частина URL-адреси, унікальна для кожного поста
    content = models.TextField(verbose_name="Вміст") # Основний текст поста
    image = models.ImageField(upload_to='blog_images/', verbose_name="Зображення для поста", blank=True, null=True) # Картинка до поста, не обов'язкова
    
    # --- ІНФОРМАЦІЯ ПРО АВТОРА ---
    author = models.ForeignKey( 
        User, # Зв'язок зі стандартною моделлю користувачів Django
        on_delete=models.SET_NULL, # Якщо автора видалять, то пост не видалиться, а поле автора просто стане порожнім (NULL)
        null=True, # Дозволяє цьому полю бути порожнім в базі даних (важливо для анонімних постів)
        blank=True, # Дозволяє не заповнювати це поле в формах (наприклад, в адмінці, якщо пост анонімний)
        related_name='blog_posts', # Дозволяє легко отримувати всі пости конкретного юзера (наприклад, user.blog_posts.all())
        verbose_name="Автор" # Назва поля в адмінці
    )
    
    # --- СТАТУС І ДАТИ ---
    status = models.CharField( 
        max_length=10, 
        choices=STATUS_CHOICES, # Вибір буде з тих, що ми визначили вище ('draft' або 'published')
        default='draft', # За замовчуванням пост буде чернеткою
        verbose_name="Статус публікації"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення") # Джанго сам поставить поточний час при створенні і більше не змінить
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публікації") # Дата, коли пост має бути опублікований, за замовчуванням - зараз

    # --- ДОДАТКОВІ НАЛАШТУВАННЯ МОДЕЛІ (МЕТАДАНІ) ---
    class Meta:
        verbose_name = "Публікація блогу" # Назва моделі в однині для адмінки
        verbose_name_plural = "Публікації блогу" # Назва моделі у множині для адмінки
        ordering = ['-published_at'] # Пости будуть сортуватися по даті публікації (спочатку новіші)

    # --- ЯК ПОСТ БУДЕ ПОКАЗУВАТИСЬ У ВИГЛЯДІ РЯДКА ---
    def __str__(self): # Цей метод визначає, як об'єкт моделі буде представлений у вигляді тексту
        return self.title # Наприклад, в адмінці ти будеш бачити заголовок поста