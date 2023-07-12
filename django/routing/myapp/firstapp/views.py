from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def about(request, title):
    template = loader.get_template('about.html')
    context = { 'title': title }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('overview.html')
    return HttpResponse(template.render())