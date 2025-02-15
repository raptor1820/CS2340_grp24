from django.core.management.base import BaseCommand

from movies.models import Movie

class Command(BaseCommand):
    help = 'Wipe the database of movies'
    def handle(self, *args, **options):
        self.stdout.write('Wiping movies from DB...')
        Movie.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Wipe done.'))