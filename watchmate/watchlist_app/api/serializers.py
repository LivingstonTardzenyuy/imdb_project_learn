from rest_framework import serializers


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = true) 
    name = serializers.CharField() 
    description = serializers.CharField() 
    active = serializers.BooleanField()