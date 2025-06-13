from rest_framework import serializers
from .models import Order, OrderItem
from shop.models import Product, Combo


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=False,
        allow_null=True
    )
    combo = serializers.PrimaryKeyRelatedField(
        queryset=Combo.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'combo', 'quantity']

    def validate(self, attrs):
        product = attrs.get('product')
        combo = attrs.get('combo')

        if not product and not combo:
            raise serializers.ValidationError("Необходимо указать либо продукт, либо комбо.")
        if product and combo:
            raise serializers.ValidationError("Нельзя выбрать одновременно продукт и комбо.")
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'client_name',
            'client_phone',
            'client_address',
            'courier',
            'status',
            'payment_method',
            'payment_status',
            'payment_id',
            'payment_amount',
            'created_at',
            'updated_at',
            'items',
            'total_price',
        ]
        read_only_fields = ['status', 'payment_status', 'payment_id', 'created_at', 'updated_at', 'total_price']

    def get_total_price(self, obj):
        return obj.calculate_total_price()

    def validate_client_phone(self, value):
        if not value.startswith('+996') or len(value) != 13:
            raise serializers.ValidationError("Телефон должен быть в формате +996XXXXXXXXX")
        return value

    def validate_payment_method(self, value):
        valid_methods = dict(Order.PAYMENT_METHOD_CHOICES)
        if value not in valid_methods:
            raise serializers.ValidationError("Недопустимый способ оплаты.")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        
        total = order.calculate_total_price()
        order.payment_amount = total if order.payment_method == 'cash' else None
        order.save()

        return order
