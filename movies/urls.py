from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'movies.index'),
    path('about/', views.about, name = 'movies.about'),
]