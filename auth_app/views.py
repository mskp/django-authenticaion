from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse

@user_passes_test(lambda user: not user.is_authenticated, login_url='home')
def login_view(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'login.html')
    except Exception as e:
        print(e)
        return redirect('/login')

@user_passes_test(lambda user: not user.is_authenticated, login_url='home')
def signup_view(request):
    try:
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
                user.save()
                return redirect('/login')
            else:
                # Passwords didn't match
                return render(request, 'signup.html', {'error': 'Passwords do not match'})

        return render(request, 'signup.html')
    except Exception as e:
        print(e)
        return redirect('/signup')

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="login")
def home(request):
    return render(request, 'index.html', {'user': request.user})
