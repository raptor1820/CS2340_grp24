from movies.models import Movie
from django.shortcuts import render

def index(request):
    searchTerm = request.GET.get('search')
    if searchTerm:
        movies = Movie.objects.filter(name_icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    templateData = {}
    templateData['title'] = 'Movies'
    templateData['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': templateData})

#Grab movie with associated id from list, pass
#that movie's name and id to movies/show.html template
def show(request, id):
    movie = Movie.objects.get(id=id)
    templateData = {}
    templateData['title'] = movie.name
    templateData['movie'] = movie
    return render(request, 'movies/show.html', {'template_data': templateData})