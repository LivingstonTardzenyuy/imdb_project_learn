from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatForm, Reviews


# class ReviewsSerializer(serializers.ModelSerializer):
    
class WatchListSerializer(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField()  #adding a new field without specifying in models.
    class Meta:
        model = WatchList 
        fields = '__all__'       
    def get_len_names(self, object):
        return len(object.name)

        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different")
        else:
            return data 
        
class StreamPlatFormSerializer(serializers.ModelSerializer):
        # watchlist = serializers.HyperlinkedRelatedField(
    #     read_only = True, many = True, view_name = 'movie-detail')  #doing the reverse relationship
    watchlist = WatchListSerializer(many = True, read_only = True)  
    class Meta:
    
        model = StreamPlatForm
        fields = "__all__"
        
        def validate(self, data):
            if data['name'] == data['about']:
                raise serializers.ValidationError("Both fields should be different")
            else:
                return data 

