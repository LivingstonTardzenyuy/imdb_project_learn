from watchlist_app.models import Movie, StreamPlatForm
from watchlist_app.api.serializers import MovieSerializer, StreamPlatFormSerializer 
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status 


from rest_framework.views import APIView 

class StreamPlatFormAV(APIView):
    def get(self, request):
        streamPlatForm = StreamPlatForm.objects.all()
        serializer = StreamPlatFormSerializer(streamPlatForm, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatFormSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)   
       
class StreamPlatFormDetailsAV(APIView):
    def get(self, request, pk):
        try:
            streamPlatForm = StreamPlatForm.objects.get(pk = pk)
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
    
class MovieListAV(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        # return Response(status = status.HTTP_200_OK)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else: 
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status = status.HTTP_200_OK)