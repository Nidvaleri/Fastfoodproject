from rest_framework import serializers
from .models import Order, OrderItem
import re


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'combo', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id', 'client_name', 'client_phone', 'client_address',
            'courier', 'status', 'created_at', 'updated_at', 'items'
        ]

    def validate_client_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно содержать минимум 2 символа")
        return value

    def validate_client_phone(self, value):
        if not re.match(r'^\+996\d{9}$', value):
            raise serializers.ValidationError("Телефон должен быть в формате +996XXXXXXXXX")
        return value

    def validate_client_address(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Адрес должен содержать минимум 5 символов")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
