from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.honeytip, name='honeytip'),
    path('suggestnew', views.suggestnew, name='suggestnew'),
    path('suggestcreate', views.suggestcreate, name='suggestcreate'),
    #path('/<int:post_id>', views.scrap, name='scrap'),
]