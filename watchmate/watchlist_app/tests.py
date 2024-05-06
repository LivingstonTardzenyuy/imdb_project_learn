from rest_framework.test import APITestCase
from django.urls import reverse 
from rest_framework import status
from rest_framework.authtoken.models import Token 
from watchlist_app.models import StreamPlatForm


class StreamPlatFormTestCase(APITestCase):
    # def setUp(self):
    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "Netflix",
            "website": "http://netflix.com"
        }
        
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)