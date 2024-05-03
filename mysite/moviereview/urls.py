from django.urls import path
from .views import HomePageView, FetchMovieData, MovieDetail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', FetchMovieData.as_view(), name='search_movie'),
    path('movie/<str:imdb_id>/', MovieDetail.as_view(), name='movie_detail'),
]
