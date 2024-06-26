from watchlist_app.models import WatchList, StreamPlatForm, Reviews
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatFormSerializer, ReviewsSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins 
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions  import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from watchlist_app.api.throttle import ReviewListThrottle, ReviewCreateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from watchlist_app.api.paginations import WatchListPagination, WatchListLimitOffsetPagination, WatchListCurserPagination

class UserReview(generics.ListAPIView):
    serializer_class = ReviewsSerializer
    # def get_queryset(self):
    #     username = self.kwargs.get('username')
    #     # movie = WatchList.objects.get(pk=pk)
    #     return Reviews.objects.filter(review_user__username = username)
    def get_queryset(self):
        queryset = Reviews.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(review_user__username = username)
        return queryset
class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewsSerializer
    throttle_classes = [ReviewCreateThrottle]
    # permission_classes = [IsReviewUserOrReadOnly]
    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        review_user = self.request.user

        #filters the reivew based on review_user and watchlist and check if user has reviewed a review
        review_queryset = Reviews.objects.filter(review_user=review_user, watchlist = movie)
        if (review_queryset.exists()):
            raise ValidationError("You have already reviewed this movie")
        
        #Calculating average rating and number of ratings
        if movie.number_rating == 0:
            movie.average_rating = serializer.validated_data['rating']
        else:
            movie.average_rating = (serializer.validated_data['rating'] + movie.average_rating) /2
            movie.number_rating  = movie.number_rating +1 
        movie.save() 
        serializer.save(watchlist = movie, review_user = review_user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
class ReviewList(generics.ListAPIView):
    throttle_classes = [ReviewListThrottle]
    # queryset = Reviews.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'review_user__username']

        
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    throttle_classes = [ScopedRateThrottle]
class StreamPlatFormAV(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [AllowAny]
    serializer_class = StreamPlatFormSerializer
    queryset = StreamPlatForm.objects.all()

class StreamPlatFormDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            streamPlatForm = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatFormSerializer(streamPlatForm)
        # return Response(status = status.HTTP_200_OK)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            StreamPlatForm = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatForm(StreamPlatForm, data = request.data)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        try: 
            streamPlatForm = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND) 
        streamPlatForm.delete()
        return Response(status = status.HTTP_200_OK)


class WatchListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    pagination_class = WatchListCurserPagination
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['name', 'platForm__name']    
    filter_backends = [filters.OrderingFilter]
    search_fields = ['^name', 'average_rating']
    
# class WatchListListAV(APIView):
#     permission_classes = [IsAuthenticated]
#     pagination_class = WatchListPagination
#     def get(self, request):
#         movie = WatchList.objects.all()
#         serializer = WatchListSerializer(movie, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = WatchListSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         else:
#             return Response(status = status.HTTP_400_BAD_REQUEST)

class WatchListListAV(viewsets.ViewSet):
    pagination_class = WatchListPagination
    def list(self, request):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie, many = True)
        return Response(serializer.data)
    def create(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
class WatchListDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        # return Response(status = status.HTTP_200_OK)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else: 
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status = status.HTTP_200_OK)