from django.urls import path
from . import views

urlpatterns = [
    path('', views.link, name='link'),
    path('coloring/', views.coloring, name='coloring'),
    path('icon/', views.icon, name='icon'),
    path('abroad/', views.abroad, name='abroad'),
    path('font/', views.font, name='font'),
] 