from rest_framework.test import APITestCase
from django.urls import reverse 
from rest_framework import status
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
        

class LoginLogOutTestCase(APITestCase):
    def setUp(self):        #this method is called before any othe test methods are called. 
       
       #this data is stored in our temporal database storage
        self.user = User.objects.create_user(
            username= "Kongnyuy",
            password= "TypeScript01@"
        )
        
    def test_loginUser(self):
        #data the user is sending from FrontEnd
        data = {
            "username": "Kongnyuy",
            "password": "TypeScript01@"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # def test_logOut(self):
    #     self.token = Token.objects.get(user__username = "Kongnyuy")
    #     self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key) # carrying my token in my headers
        
    #     response = self.client.post(reverse('logout'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        