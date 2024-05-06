from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from watchlist_app.models import *

from watchlist_app.api import serializers 
from watchlist_app import models
from rest_framework.request import Request

# class StreamPlatFormTestCase(APITestCase):
#     def setUp(self):
        
#         #creating a new user
#         self.user =  User.objects.create(
#             username="Kongnyuy",
#             password="Password@123",
#         )
#         self.token = Token.objects.get(user__username=self.user)    #create a new token
#         # client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  #carrying the token into

#     def test_streamplatform_get(self):
#         response = self.client.get(reverse('streamplatform-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_streamplatform_create(self):
#         data = {
#             "name": "Netflix",
#             "about": "Netflix",
#             "website": "http://netflix.com"
#         }
#         response = self.client.post(reverse('streamplatform-list'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = "example", password = "Password@123")
        #Login in a user. 
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        
        self.stream = StreamPlatForm.objects.create(
            name = "netflix",
            about = ""
        )
        
    def test_streamPlatFormCreate(self):
        data = {
            "name": "kongyuylivingston",
            "about": "best movie on earth",
            "website": "www.kongnyuy.com",
        }
        
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_streamplatform_id(self):
        response = self.client.get(reverse('streamplatform-detail', args = (self.stream.id,)))      #args allow me to access the individual elements. 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    