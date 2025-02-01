from django.db import models

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
        return f"{self.name} has id:{self.id}, a price of ${price}, and a description: {description}."