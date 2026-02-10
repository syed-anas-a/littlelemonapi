from django.urls import path, include
from . import views

urlpatterns = [
    #User registration and token generation endpoints 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    #MenuItemview
    path('menu-items/', views.MenuItemListCreate.as_view())
]