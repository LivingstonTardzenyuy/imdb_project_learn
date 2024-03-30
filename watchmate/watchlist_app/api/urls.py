from django.urls import path 
from watchlist_app.api.views import (
    WatchListListAV, WatchListDetailsAV, 
    StreamPlatFormAV, StreamPlatFormDetailsAV, 
    ReviewList, ReviewDetails)
urlpatterns = [
    path('list/',  WatchListListAV.as_view(), name = 'movie list'),
    path('list/<int:pk>', WatchListDetailsAV.as_view(), name = 'movie-detail'),
    
    path('streamPlatForm/', StreamPlatFormAV.as_view(), name = "streamPlatform"),
    path('streamPlatForm/<int:pk>', StreamPlatFormDetailsAV.as_view(), name = 'streamplatform details'),
    
    path('stream/li')
    
    path('reviews', ReviewList.as_view(), name = 'review-list'),  
    path('reviews/<int:pk>', ReviewDetails.as_view(), name = 'retrieve-reviews')
]
