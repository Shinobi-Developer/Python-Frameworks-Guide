from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required

from .models import Users

@csrf_protect

# Create your views here.
def about(request, title):
    template = loader.get_template('about.html')
    context = { 'title': title }
    return HttpResponse(template.render(context, request))

@login_required
def index(request):
    template = loader.get_template('overview.html')
    return HttpResponse(template.render())

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        lower_email = email.lower()
        user = authenticate(request, email = lower_email, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return render(request, 'auth/login.html')
    
    return render(request, 'auth/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            if Users.objects.filter(username = username).exists():
                messages.info(request, 'User is already exists')
                return render(request, 'auth/register.html')
            if Users.objects.filter(email = email).exists():
                messages.info(request, 'Email is already taken')
                return render(request, 'auth/register.html')
            
            user = get_user_model().objects.create_user(username = username, email=email.lower())
            user.name = name
            user.age = age
            user.set_password(password)
            user.is_active = True
            user.save()
            return render(request, 'auth/login.html')
        else:
            messages.info(request, 'Password is not match')
            return render(request, 'auth/register.html')
        
    return render(request, 'auth/register.html')

def logout_view(request):
    logout(request)
    return render(request, 'auth/login.html')