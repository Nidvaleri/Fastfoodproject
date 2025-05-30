from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес доставки")

    def __str__(self):
        return f"{self.name} ({self.phone})"

class CartItem(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")

    def __str__(self):
        return f"{self.product.name} x {self.quantity} для {self.client.full_name}"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время заказа")
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('confirmed', 'Подтверждён'),
        ('preparing', 'Готовится'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус заказа")

    def __str__(self):
        return f"Заказ #{self.id} для {self.client.full_name} ({self.get_status_display()})"
