from .models import MenuItem, Cart
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerialzer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type':'password'})
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

    def create(self, validated_data):
        menuitem = validated_data['menuitem']
        quantity = validated_data['quantity']
        validated_data['price'] = menuitem.price * quantity
        return super().create(validated_data)

    
