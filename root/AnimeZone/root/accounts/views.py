from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse

def signup_view(request):
<<<<<<< HEAD
    if request.user.is_authenticated:
        return redirect('home:index') 

=======
    """
    View для реєстрації нових користувачів зі стандартною формою Django
    """
    if request.user.is_authenticated:
        return redirect('index')
    
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get('username')
<<<<<<< HEAD
                messages.success(request, f'Аккаунт створено для {username}!')
                login(request, user)
                return redirect('home:index') 
            except Exception as e:
                messages.error(request, f'Помилка при створенні акаунта: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{form.fields[field].label}: {error}')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:index')  

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Ласкаво просимо, {user.username}!')
                return redirect(request.GET.get('next') or 'home:index')  
=======
                messages.success(
                    request, 
                    f'Аккаунт створено для {username}! Тепер ви можете увійти.'
                )
                # Логируем пользователя сразу после регистрации
                login(request, user)
                return redirect('index')  # Перенаправляем на главную
            except Exception as e:
                messages.error(request, f'Помилка при створенні акаунта: {str(e)}')
        else:
            # Показываем ошибки формы
            for field, errors in form.errors.items():
                field_name = form.fields[field].label or field
                for error in errors:
                    messages.error(request, f'{field_name}: {error}')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    """
    View для входу користувача зі стандартною формою Django
    """
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Ласкаво просимо, {username}!')
                
                # Перенаправлення після входу
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('index')
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
            else:
                messages.error(request, 'Невірне ім\'я користувача або пароль.')
        else:
            messages.error(request, 'Будь ласка, виправте помилки в формі.')
    else:
        form = AuthenticationForm()
<<<<<<< HEAD

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.info(request, f'До побачення, {username}!')
    return redirect('home:index') 


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
=======
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """
    View для виходу користувача з системи
    """
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.info(request, f'До побачення, {username}! Ви успішно вийшли з системи.')
    return redirect('index')

@login_required
def profile_view(request):
    """
    View для відображення профілю користувача
    """
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })
>>>>>>> 9b57fad859342b59893408cc7b228fa1c821b3d6
