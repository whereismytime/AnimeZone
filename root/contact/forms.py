from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Ім'я",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Ваш email'})
    )
    message = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder':'Ваше повідомлення'})
    )
