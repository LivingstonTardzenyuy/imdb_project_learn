from django.urls import path 
from rest_framework.authtoken import views
from users_app.api.views import registration_view, logout_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView,)


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

