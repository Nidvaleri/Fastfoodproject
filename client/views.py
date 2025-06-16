from rest_framework import generics
from .models import Client, CartItem, Order
from .serializers import ClientSerializer, CartItemSerializer, OrderSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CartItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self): # Метод для получения queryset (набора данных)
        client_id = self.kwargs['client_id']
        return CartItem.objects.filter(client_id=client_id)

    def perform_create(self, serializer):  # Метод вызывается при создании нового объекта
        client_id = self.kwargs['client_id']
        serializer.save(client_id=client_id)

class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

