from django.urls import path , include
from watchlist_app.api.views import (
    WatchListListAV, WatchListDetailsAV, StreamPlatFormAV,
    ReviewList, ReviewDetails, ReviewCreate)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatFormAV, basename="streamplatform")


urlpatterns = [
    path('list/',  WatchListListAV.as_view(), name = 'movie list'),
    path('list/<int:pk>', WatchListDetailsAV.as_view(), name = 'movie-detail'),
    
    path('', include(router.urls)),
    
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'review-list'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'review-create'),
    path('stream/review/<int:pk>', ReviewDetails.as_view(), name = 'review-reviews')
    
]
