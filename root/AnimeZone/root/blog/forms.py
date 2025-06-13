# blog/forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  
        fields = ['title', 'content', 'image'] # Які поля з моделі ми хочемо бачити у формі


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Напишіть свій пост тут...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
