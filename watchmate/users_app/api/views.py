from users_app.api.serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view 
from rest_framework import status 
from rest_framework.response import Response 


@api_view(['POST'],)
def registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        response = {}
        if serializer.is_valid():
            response['response'] ='Registered successfully'
            username = serializer.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        response['response'] = 'Registration registration failed'
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)