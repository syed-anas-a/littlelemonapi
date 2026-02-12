from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsManager, IsDeliveryCrew
from django.contrib.auth.models import User


# Create your views here.

# Group views
class GroupManagementView(generics.ListCreateAPIView):
    
    ...


# Menu-item views
class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 
    permission_classes = [IsManager, IsDeliveryCrew]
    

class MenuItemRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'pk'
    permission_classes = [IsManager]

    


