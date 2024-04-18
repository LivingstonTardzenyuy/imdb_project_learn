from users_app.api.serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view 
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from users_app.models import *

@api_view(['POST'],)
def registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
       
        
        data = {}
        if serializer.is_valid():
            data['response'] ='Registered successfully'
            account = serializer.save()
            data['username'] = account.username
            data['emal'] = account.email
            token = Token.objects.get(user = account).key
            data['token'] = token 
            # return Response(data, status=status.HTTP_201_CREATED) q 
        else:
            data['response'] = serializer.errors
        return Response(data)
    

@api_view(['POST'],)
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    