from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomePageView, FetchMovieData, MovieDetail, MyPortalView, ReviewedMoviesView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('myportal/', MyPortalView.as_view(), name='myportal'),
    path('search/', FetchMovieData.as_view(), name='search_movie'),
    path('movie/<str:imdb_id>/', MovieDetail.as_view(), name='movie_detail'),
    path('reviewed-movies/', ReviewedMoviesView.as_view(), name='reviewed_movies'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='moviereview/registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
