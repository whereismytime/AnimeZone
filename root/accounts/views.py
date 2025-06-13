from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse

def signup_view(request):
    """
    View for registering new users using Django's default UserCreationForm.
    """
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, 
                    f'Account created for {username}! Now you can log in.'
                )
                login(request, user)
                return redirect('index')  # Redirect to the home page
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
        else:
            # Show form errors
            for field, errors in form.errors.items():
                field_name = form.fields[field].label or field
                for error in errors:
                    messages.error(request, f'{field_name}: {error}')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    """
    View for logging in a user using Django's default AuthenticationForm.
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
                messages.success(request, f'Welcome, {username}!')
                
                # Redirect after login
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """
    View for logging out a user.
    """
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.info(request, f'Goodbye, {username}! You have successfully logged out.')
    return redirect('index')

@login_required
def profile_view(request):
    """
    View for displaying the user's profile.
    """
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })
