from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    #Auto-assigned, uses positive integers
    id = models.AutoField(primary_key=True)
    #String
    name = models.CharField(max_length=255)
    #Integer
    price = models.IntegerField()
    #Text field, no limit
    description = models.TextField()
    #Image
    image = models.ImageField(upload_to='movies_images/')

    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    #Auto-assigned natural
    id = models.AutoField(primary_key=True)
    #Actual review
    comment = models.CharField(max_length=500)
    #Date of review
    date = models.DateTimeField(auto_now_add=True)
    #Movie being reviewed
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #User who made review
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} reviewed {self.movie.name}"