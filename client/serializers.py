from rest_framework import serializers
from .models import Client, CartItem, Order
from shop.serializers import ProductSerializer
from shop.models import Product
import re


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone', 'address']

    def validate_name(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Имя должно содержать только буквы.")
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно быть не короче 2 символов.")
        return value

    def validate_phone(self, value):
        if not re.match(r'^\+996\d{9}$', value):
            raise serializers.ValidationError("Телефон должен быть в формате +996XXXXXXXXX.")
        return value

    def validate_address(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Адрес должен содержать минимум 5 символов.")
        return value


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'client', 'product', 'product_id', 'quantity', 'added_at']
        read_only_fields = ['id', 'added_at']
        ref_name = 'ClientCartItemSerializer'


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source='client',
        write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'client', 'client_id', 'created_at', 'status']
        read_only_fields = ['id', 'created_at', 'status']
