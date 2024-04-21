from django.urls import path 
from rest_framework.authtoken import views
from users_app.api.views import registration_view, logout_view

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
]
