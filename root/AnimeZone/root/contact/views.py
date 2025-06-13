from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # тут можно отправить email или сохранить в БД
            messages.success(request, 'Дякуємо! Ваше повідомлення надіслано.')
            return redirect('contact:contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form
    })
