from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/<str:title>', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]