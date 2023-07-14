from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/<str:title>', views.about, name='about'),
    path('login/', views.signin, name='signin'),
    path('register/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout')
]