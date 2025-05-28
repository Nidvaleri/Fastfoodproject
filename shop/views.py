from rest_framework import viewsets
from .models import Category, Product, Cart, CartItem, Discount, Combo, Review
from .serializers import (
    CategorySerializer, ProductSerializer, CartSerializer,
    CartItemSerializer, DiscountSerializer, ComboSerializer, ReviewSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product')
        if product_id:
            return self.queryset.filter(product_id=product_id)
        return self.queryset

# Create your views here.
