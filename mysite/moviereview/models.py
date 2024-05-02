from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    imdb_id = models.CharField(max_length=20, unique=True)
    imdb_rating = models.FloatField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=255)  # Simplified for example
    stars = models.TextField()  # Text field to store list of names
    directors = models.TextField()  # Text field to store list of names
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title
