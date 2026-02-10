from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.

class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 

    def get_permissions(self):
        if(self.request.method == 'POST'):
            return [IsAdminUser()]
        else:
            [IsAuthenticatedOrReadOnly()]

class MenuItemRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'item'

    


