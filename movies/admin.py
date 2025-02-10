from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    searchFields = ['name']

admin.site.register(Movie)
admin.site.register(Review)