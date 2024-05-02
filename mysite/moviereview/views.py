from django.views import View
from django.shortcuts import render, redirect
from .forms import MovieIDForm
from .models import Movie
from django.core.files.base import ContentFile
import requests


class FetchMovieData(View):
    form_class = MovieIDForm
    template_name = 'moviereview/home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            imdb_id = form.cleaned_data['imdb_id']
            movie_details = self.fetch_movie_details(imdb_id)
            poster_url = self.fetch_movie_poster(imdb_id)

            stars = movie_details.get('stars', [])[:5]
            directors = movie_details.get('directors', [])[:5]

            movie = Movie(
                title=movie_details.get('title', ''),
                description=movie_details.get('description', ''),
                release_date=movie_details.get('release_date', '1900-01-01'),
                imdb_id=imdb_id,
                imdb_rating=float(movie_details.get('imdb_rating', 0.0)),
                runtime=int(movie_details.get('runtime', 0)),
                genres=", ".join(movie_details.get('genres', [])),
                stars=", ".join(stars),
                directors=", ".join(directors),
            )

            response = requests.get(poster_url)
            if response.status_code == 200:
                movie.poster.save(f"{imdb_id}_poster.jpg", ContentFile(response.content), save=False)
            movie.save()

            return redirect('movie_detail', imdb_id=imdb_id)
        return render(request, self.template_name, {'form': form})

    def fetch_movie_details(self, imdb_id):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"
        querystring = {"movieid": imdb_id}
        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            return {}  # Return an empty dictionary if there's an error

    def fetch_movie_poster(self, imdb_id):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"
        querystring = {"movieid": imdb_id}
        headers = {
            "Type": "get-movies-images-by-imdb",
            "X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            poster_data = response.json()
            return poster_data.get('poster', '')  # Safely return the poster URL or an empty string
        else:
            return ''  # Return an empty string if there's an error


class MovieDetail(View):
    template_name = 'moviereview/movie_detail.html'

    def get(self, request, imdb_id, *args, **kwargs):
        movie = Movie.objects.get(imdb_id=imdb_id)
        return render(request, self.template_name, {'movie': movie})
