from django.shortcuts import render

#Movies is a list of dictionaries, every movie in movies should have:
#an integer id, name, price, and description at minimum

movies = []

#Renders the movies/index.html template
def index(request):
    templateData = {}
    templateData['title'] = 'Movies'
    templateData['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': templateData})

#Grab movie with associated id from list, pass
#that movie's name and id to movies/show.html template
def show(request, id):
    movie = movies[id - 1]
    templateData = {}
    templateData['title'] = movie['name']
    templateData['movie'] = movie
    return render(request, 'movies/show.html', {'template_data': templateData})
