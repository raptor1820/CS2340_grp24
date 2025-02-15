from django.core.management.base import BaseCommand
import os
import environ
from pathlib import Path
from movies.models import Movie
import requests
class Command(BaseCommand):
    help = 'Populate the database with movies. Check for API key in .env file'

    def handle(self, *args, **options):
        self.stdout.write('Populating DB...')
        IMAGE_BASE_PATH = "https://image.tmdb.org/t/p/w500"
        BASE_DIR = Path(__file__).resolve().parent.parent
        First = True

        env = environ.Env(
            # Set default values and casting
            DEBUG=(bool, False)
        )

        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": env('AUTHENTICATION')
        }

        response = requests.get(url, headers=headers)
        response = response.json()

        for i in response["results"]:
            movie = Movie()
            movie.price = 10
            movie.name = i['title']
            movie.description = i['overview']
            movie.image = IMAGE_BASE_PATH + i['poster_path']
            movie.save()
        self.stdout.write(self.style.SUCCESS('Population done.'))