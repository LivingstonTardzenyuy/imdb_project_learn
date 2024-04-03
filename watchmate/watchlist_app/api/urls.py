from django.urls import path 
from watchlist_app.api.views import (
    WatchListListAV, WatchListDetailsAV, 
    StreamPlatFormAV, StreamPlatFormDetailsAV, 
    ReviewList, ReviewDetails, ReviewCreate)
urlpatterns = [
    path('list/',  WatchListListAV.as_view(), name = 'movie list'),
    path('list/<int:pk>', WatchListDetailsAV.as_view(), name = 'movie-detail'),
    
    path('streamPlatForm/', StreamPlatFormAV.as_view(), name = "streamPlatform"),
    path('streamPlatForm/<int:pk>', StreamPlatFormDetailsAV.as_view(), name = 'streamplatform details'),
    
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'review-list'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'review-create'),
    path('stream/review/<int:pk>', ReviewDetails.as_view(), name = 'review-reviews')
    
]
