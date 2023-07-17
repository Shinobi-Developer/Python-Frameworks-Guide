from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('remove/<str:id>', views.remove, name='remove')
]