from rest_framework import serializers
from .models import Client, CartItem, Order
from shop.serializers import ProductSerializer
from shop.models import Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone', 'address']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # детальная инфо о товаре
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'client', 'product', 'product_id', 'quantity', 'added_at']
        read_only_fields = ['id', 'added_at']

class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)  # показываем данные клиента
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), source='client', write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'client_id', 'created_at', 'status']
        read_only_fields = ['id', 'created_at', 'status']
