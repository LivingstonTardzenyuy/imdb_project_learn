from django.urls import path 
from watchlist_app.api.views import WatchListListAV, WatchListDetailsAV, StreamPlatFormAV, StreamPlatFormDetailsAV
urlpatterns = [
    path('list/',  WatchListListAV.as_view(), name = 'movie list'),
    path('list/<int:pk>', WatchListDetailsAV.as_view(), name = 'movie detail'),
    
    path('streamPlatform/', StreamPlatFormAV.as_view(), name = "streamPlatform"),
    path('streamPlatForm/<int:pk>', StreamPlatFormDetailsAV.as_view(), name = 'stream platform details')    
]
