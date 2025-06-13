from rest_framework import serializers
from .models import Category, Product, Cart, CartItem, Discount, Combo, Review

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )

    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    weight = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля")
        return value

    def validate_weight(self, value):
        if value <= 0:
            raise serializers.ValidationError("Вес должен быть больше нуля")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Количество не может быть отрицательным")
        return value

    class Meta:
        model = Product
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    percentage = serializers.IntegerField()

    def validate_percentage(self, value):
        if not (1 <= value <= 100):
            raise serializers.ValidationError("Скидка должна быть от 1 до 100 процентов")
        return value

    class Meta:
        model = Discount
        fields = '__all__'


class ComboSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля")
        return value

    class Meta:
        model = Combo
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    quantity = serializers.IntegerField()

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество должно быть не меньше 1")
        return value

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        ref_name = 'ShopCartItemSerializer'


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Рейтинг должен быть от 1 до 5")
        return value

    class Meta:
        model = Review
        fields = ['id', 'product', 'author_name', 'text', 'rating', 'created_at']
