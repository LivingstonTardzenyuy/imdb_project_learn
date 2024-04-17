from rest_framework import serializers 
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(
        style={
            'input_type':'password'
        },
        write_only = True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)
        extra_kwargs ={
            'password': {'write_only': True}
        }    
    
    def save(self):
        email_user = self.validated_data.get('email')
        password = self.validated_data.get('password')
        password_confirmation = self.validated_data.get('password_confirmation')
        username = self.validated_data.get('username')
        print(password)
        print(password_confirmation)
        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match")
        
        if User.objects.filter(email = email_user).exists():
            raise serializers.ValidationError("Email already exists")

        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError("Username already exists")
        
        account = User(
            username = username,
            email = email_user
        )
        account.set_password(password)
        account.save()
        
        return account