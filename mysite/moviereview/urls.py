from django.urls import path
from .views import FetchMovieData, MovieDetail

urlpatterns = [
    path('', FetchMovieData.as_view(), name='home'),
    path('movie/<str:imdb_id>/', MovieDetail.as_view(), name='movie_detail'),
]
