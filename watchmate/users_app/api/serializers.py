from rest_framework import serializers 
from django.contrib.auth.models import User


class UserRegistration(serializers.ModelSerializer):
    password_confirmation = serializers.StringRelatedField(write_only = True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)
        
    
    def save(self):
        