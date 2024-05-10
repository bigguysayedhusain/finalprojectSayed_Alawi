from django.db import models
from django.conf import settings
from django.utils.timezone import localtime


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    imdb_id = models.CharField(max_length=20, unique=True)
    imdb_rating = models.FloatField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=255)
    stars = models.TextField()
    directors = models.TextField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 11)])  # Rating from 1 to 10
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Format the date to a more readable form, e.g., "March 10, 2021"
        formatted_date = localtime(self.created_at).strftime('%B %d, %Y')
        return f"{self.user.username}'s review of {self.movie.title} on {formatted_date}"
