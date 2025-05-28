from rest_framework import serializers
from .models import Courier

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['id', 'full_name', 'phone', 'is_active', 'delivery_zone', 'shop']  # Поля для сериализации
