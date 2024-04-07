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
from rest_framework.permissions import IsAuthenticated

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializer
    
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
        serializer.save(watchlist = movie, review_user = review_user)
        
class ReviewList(generics.ListAPIView):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    


# class StreamPlatFormAV(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatForm.objects.all()
#         serializer = StreamPlatFormSerializer(queryset, many = True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatForm.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatFormSerializer(watchlist)
#         return Response(serializer.data)


#     def create(self, request):
#         serializer = StreamPlatFormSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)

#     def destroy(self, requet, pk=None):
#         try:
#             streamPlatForm = StreamPlatForm.objects.get(pk=pk)
#         except StreamPlatForm.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)
#         streamPlatForm.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 

class StreamPlatFormAV(viewsets.ModelViewSet):
    serializer_class = StreamPlatFormSerializer
    queryset = StreamPlatForm.objects.all()

class StreamPlatFormDetailsAV(APIView):
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
    
class WatchListListAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class WatchListDetailsAV(APIView):
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