from movies.models import Movie, Review
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pathlib import Path
import requests
import environ
import os
#dummy change
IMAGE_BASE_PATH = "https://image.tmdb.org/t/p/w500"
BASE_DIR = Path(__file__).resolve().parent.parent
First = True

env = environ.Env(
    # Set default values and casting
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def populate_database():
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

#Renders the movies/index.html template
def index(request):
    # if not hasattr(index, "first_time"):
    #     index.first_time = True  # Initialize attribute
    #
    # if index.first_time:
    #     populate_database()
    #     print("dataset populated")
    #     index.first_time = False  # Prevent future execution

    searchTerm = request.GET.get('search')
    if searchTerm:
        movies = Movie.objects.filter(name__icontains=searchTerm)
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
    reviews = Review.objects.filter(movie=movie)
    templateData = {}
    templateData['title'] = movie.name
    templateData['movie'] = movie
    templateData['reviews'] = reviews
    return render(request, 'movies/show.html', {'template_data': templateData})

@login_required
def createReview(request, id):
    #If comment isn't blank and user is trying to upload review
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        #Initialize blank review
        review = Review()
        #Assign comment
        review.comment = request.POST['comment']
        #Assign movie
        review.movie = movie
        #Assign user
        review.user = request.user
        #Save the review
        review.save()
        return redirect('movies.show', id=id)
    else:
        #Failure, return to movie page
        return redirect('movies.show', id=id)

@login_required
def editReview(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    #If user trying to edit is not the user who made the review
    #send them back to the movie page
    if request.user != review.user:
        return redirect('movies.show', id=id)
    if request.method == 'GET':
        templateData = {}
        templateData['title'] = 'Edit Review'
        templateData['review'] = review
        return render(request, 'movies/edit_review.html', {'template_data': templateData})
    #If edit is not blank, update it
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    #Send user back to the movie page
    else:
        return redirect('movies.show', id=id)

@login_required
def deleteReview(request, id, review_id):
    review = get_object_or_404(Review, id = review_id, user = request.user)
    review.delete()
    return redirect('movies.show', id=id)