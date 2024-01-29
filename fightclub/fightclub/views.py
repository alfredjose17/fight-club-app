from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Match

# Renders the home page
def home(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'home.html', context)

@login_required
def fight(request, match_id):
    match = Match.objects.get(match_id=match_id)

    if request.user.username and (match.player1_id is None or match.player2_id is None):
        if match.player1_id is None:
            match.player1_id = request.user
        elif match.player2_id is None:
            match.player2_id = request.user
        match.save()

    return redirect('/')

# Renders the login page
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    form = LoginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                auth_login(request, user)
                return redirect('/admin')
            elif user is not None and not user.is_staff:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Error validating form')
            form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')

# Renders the sign up page
def register(request):
    if(request.user.is_authenticated):
        return redirect('/')
    
    form = RegisterForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('/login')
    else:
        messages.error(request, 'Error validating form')
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
