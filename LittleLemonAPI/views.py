from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import MenuItem, Cart
from .serializers import MenuItemSerializer, CartSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .permissions import IsManager, IsDeliveryCrew
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


# Create your views here.

# Group views
class UserGroupManagement(APIView):
    permission_classes = [IsManager]

    def get_group(self, group_name):
        if group_name == "delivery-crew":
            group_name = "Delivery Crew"
        try:
            return Group.objects.get(name__icontains=group_name)
        except:
            raise NotFound("Group not found!!")

    def get(self, request, group_name):
        group = self.get_group(group_name)
        users = group.user_set.all()
        data = [{"id": user.id, "username": user.username} for user in users]
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request, group_name):
        user_id = request.data.get("user_id")
        group = self.get_group(group_name)
        try:
            user = User.objects.get(id=user_id)
        except:
            raise NotFound("User not found!!")
        group.user_set.add(user)
        return Response({"message": "User added"}, status=status.HTTP_201_CREATED)
    
    def delete(self, request, group_name, userId):
        group = self.get_group(group_name)
        user = User.objects.get(id=userId)
        try:
            group.user_set.remove(user)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

    


# Menu-item views
class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsManager()]
        return [IsAuthenticated()]
    

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'title'
    lookup_url_kwarg = 'menuItem'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsManager()]
        return [IsAuthenticatedOrReadOnly()]
    
# Cart View
class CartList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        menuitem = request.data.get('menuitem')
        quantity = int(request.data.get('quantity'))

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            menuitem_id=menuitem,
            defaults={
                'quantity': quantity,
                'price': 0
            }   
        )   

        if not created:
            cart_item.quantity += quantity

        cart_item.price = cart_item.quantity * cart_item.menuitem.price
        cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
       
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)
    

    


