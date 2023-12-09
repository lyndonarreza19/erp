from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import CustomUser, UserProfile
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.shortcuts import get_object_or_404

from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                UserProfile.objects.create(user=user)  # Create the user profile
                return redirect('user:signup_success')
            except IntegrityError:  # Catch the IntegrityError for email uniqueness
                form.add_error('email', 'A user with this email already exists.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/signup.html', {'form': form})






def signup_success(request):
    return render(request, 'user/signup_success.html')


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the desired page after successful login
            return redirect('main:index')
    else:
        form = AuthenticationForm()
    return render(request, 'user/signin.html', {'form': form})


def view_profile(request):
    user_profile = request.user.profile  # Access the user profile associated with the currently logged-in user
    # Use the user profile data as needed
    # For example: user_profile.bio, user_profile.profile_picture, etc.
    return render(request, 'user/view_profile.html', {'user_profile': user_profile})



def view_profile(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'user/view_profile.html', {'user_profile': user_profile})



def logout_view(request):
    logout(request)
    return redirect('main:index')