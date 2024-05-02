from rest_framework.test import APITestCase
from django.urls import reverse 
from rest_framework.test import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 



# Create your tests here.
class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testCase",
            "password": "NewPassword",
            "password2": "NewPassword2",
            
        }
        
        response = self.client.post(reverse("registration"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)