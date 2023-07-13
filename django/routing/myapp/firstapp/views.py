from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Users
from django.views.decorators.csrf import csrf_protect
from helper.util import isRepeated

@csrf_protect

# Create your views here.
def about(request, title):
    template = loader.get_template('about.html')
    context = { 'title': title }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('overview.html')
    return HttpResponse(template.render())

def login(request):
    if request.method == 'POST':
        email = Users.objects.filter(email = request.POST['email']).first()
        password = Users.objects.filter(password = request.POST['password']).first()
    
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        if isRepeated(request.POST['username'], request.POST['email']) is True:
            return HttpResponse('User already exists')
        
        user = Users(
            name = request.POST['name'],
            username = request.POST['username'],
            age = request.POST['age'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        user.save()
        return render(request, 'auth/login.html')
        
    return render(request, 'auth/register.html')