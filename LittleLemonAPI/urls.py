from django.urls import path
from rest_framwork import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    #User registration and token generation endpoints 
    path('api/users/', ),
    path('api/users/users/me/'),
    path('token/login/', TokenObtainPairView.as_view())
]