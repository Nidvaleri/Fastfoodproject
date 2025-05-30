from django.urls import path
from .views import (
    ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView,
    CartItemListCreateAPIView, CartItemRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView,
)
urlpatterns = [
    # Клиенты (создать нового клиента при оформлении, просмотреть список)
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-detail'),

    # Корзина для клиента: список и добавление
    path('clients/<int:client_id>/cart/', CartItemListCreateAPIView.as_view(), name='cartitem-list-create'),

    # Отдельный элемент корзины - обновить, удалить
    path('cartitems/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view(), name='cartitem-detail'),

    # Заказы
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
]
