from django.urls import path 
from watchlist_app.api.views import MovieListAV, MovieDetailsAV
urlpatterns = [
    path('list/',  MovieListAV.as_view(), name = 'movie list'),
    path('list/<int:pk>', MovieDetailsAV.as_view(), name = 'movie detail')
]
