from django.views import View, generic
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import Http404
from django.core.files.base import ContentFile
from django.urls import reverse_lazy
from django.contrib.auth import logout
import requests
from .forms import MovieSearchForm, SignUpForm
from .models import Movie


class HomePageView(TemplateView):
    template_name = 'moviereview/home.html'

class MyPortalView(TemplateView):
    template_name = 'moviereview/my_portal.html'

class FetchMovieData(View):
    form_class = MovieSearchForm
    template_name = 'moviereview/search_movie.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            supplied_movie_name = form.cleaned_data['supplied_movie_name']
            movies = self.search_movies_by_title(supplied_movie_name)
            return render(request, self.template_name, {'form': form, 'movies': movies})
        return render(request, self.template_name, {'form': form})

    def search_movies_by_title(self, movie_name):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"
        querystring = {"title": movie_name}
        headers = {
            "Type": "get-movies-by-title",
            "X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()['movie_results']
        return []


class MovieDetail(View):
    template_name = 'moviereview/movie_detail.html'

    def get(self, request, imdb_id, *args, **kwargs):
        try:
            # Try to get the movie from the database
            movie = Movie.objects.get(imdb_id=imdb_id)
            streaming_services = self.fetch_streaming_info(imdb_id)
        except Movie.DoesNotExist:
            # If the movie does not exist, fetch from API and save it
            movie_details = self.fetch_movie_details(imdb_id)
            if not movie_details:
                raise Http404("Movie not found in external database.")

            poster_url = self.fetch_movie_poster(imdb_id)
            stars = movie_details.get('stars', [])[:5]
            directors = movie_details.get('directors', [])[:5]

            # Create a new Movie instance
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

            # Fetch and save the poster if the URL is available
            if poster_url:
                response = requests.get(poster_url)
                if response.status_code == 200:
                    movie.poster.save(f"{imdb_id}_poster.jpg", ContentFile(response.content), save=True)

            movie.save()

            # Fetch streaming information every time, irrespective of database existence
            streaming_services = self.fetch_streaming_info(imdb_id)

        return render(request, self.template_name, {'movie': movie, 'streaming_services': streaming_services})

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
        return {}

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
            return response.json().get('poster', '')
        return ''

    def fetch_streaming_info(self, imdb_id):
        url = "https://streaming-availability.p.rapidapi.com/get"
        querystring = {"output_language": "en", "imdb_id": imdb_id}
        headers = {
            "X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
            "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()['result']

        us_streaming_info = data.get('streamingInfo', {}).get('us', {})

        streaming_services = []
        for service in us_streaming_info:
            if (service.get('quality', 'uhd') == "uhd") and (service['streamingType'] == "rent" or
                                                             service['streamingType'] == "subscription"):
                streaming_services.append({
                    'service': service['service'].capitalize(),
                    'link': service['link']
                })
        return streaming_services
        # return []


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'moviereview/registration/signup.html'


def logout_view(request):
    logout(request)
    return render(request, 'moviereview/registration/logout.html')
