from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('new/', views.new, name='new'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('<int:post_id>', views.detail, name="detail"),
    path('edit', views.edit, name='edit'),
    path('postupdate/<int:post_id>', views.postupdate, name='postupdate'),
    path('postdelete/<int:post_id>', views.postdelete, name='postdelete'),
    path('result/', views.result, name='result'),
    path('scrap/<int:post_id>', views.scrap, name='scrap'),
    path('empty_ppt/', views.empty_ppt, name='empty_ppt'),
    #path('search/', views.search, name='search'),
    path('pptdownload', views.ppt, name='ppt'),   
]