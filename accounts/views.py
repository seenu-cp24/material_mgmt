from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
import os


def user_login(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')


@login_required
def user_logout(request):
    """Log out the current user."""
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    """
    Dashboard with role-based visibility.
    Shows 'Add User' only for superusers.
    """
    print(">>> Logged in as:", request.user.username)
    print(">>> Is superuser:", request.user.is_superuser)

    context = {
        'is_superuser': request.user.is_superuser,
    }
    return render(request, 'accounts/dashboard.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    """
    Allow only superusers to create new users.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('add_user')

        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' already exists.")
            return redirect('add_user')

        User.objects.create_user(username=username, password=password)
        messages.success(request, f"User '{username}' created successfully.")
        return redirect('dashboard')

    return render(request, 'accounts/add_user.html')


@user_passes_test(lambda u: u.is_superuser)
def forgot_password(request):
    """
    Allow superuser to reset another user's password.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, f"Password for '{username}' has been reset successfully.")
            return redirect('dashboard')
        except User.DoesNotExist:
            messages.error(request, f"User '{username}' not found.")

    return render(request, 'accounts/forgot_password.html')
