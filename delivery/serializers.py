from rest_framework import serializers
from .models import Courier

class CourierSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        min_length=5,
        max_length=100,
        help_text="Введите полное имя (не менее 5 символов)",
        error_messages={
            "blank": "Поле 'ФИО' не может быть пустым.",
            "min_length": "ФИО должно содержать минимум 5 символов."
        }
    )

    phone = serializers.RegexField(
        regex=r'^\+996\d{9}$',
        max_length=13,
        help_text="Телефон в формате: +996XXXXXXXXX",
        error_messages={
            "invalid": "Телефон должен начинаться с +996 и содержать ровно 9 цифр после.",
            "blank": "Телефон обязателен для заполнения."
        }
    )

    delivery_zone = serializers.CharField(
        min_length=3,
        max_length=100,
        help_text="Укажите район или часть города",
        error_messages={
            "min_length": "Зона доставки должна содержать минимум 3 символа.",
            "blank": "Зона доставки не может быть пустой."
        }
    )

    class Meta:
        model = Courier
        fields = ['id', 'full_name', 'phone', 'is_active', 'delivery_zone', 'shop']
