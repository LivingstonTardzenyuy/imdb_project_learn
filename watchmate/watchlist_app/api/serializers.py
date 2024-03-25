from rest_framework import serializers
from watchlist_app.models import Movie 


class MovieSerializer(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField()  #adding a new field without specifying in models.
    class Meta:
        model = Movie 
        fields = ['name', 'description', 'active', 'len_names']


       
    def get_len_names(self, object):
        return len(object.name)

        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different")
        else:
            return data 