from django.db import models
from shop.models import Shop  # Импортируем нашу модель магазина

class Courier(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО курьера")  # Имя курьера
    phone = models.CharField(max_length=20, verbose_name="Телефон")          # Телефон для связи
    is_active = models.BooleanField(default=True, verbose_name="Активен")   # Активность курьера
    delivery_zone = models.CharField(max_length=100, verbose_name="Зона доставки")  # Зона доставки
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='couriers', verbose_name="Магазин")  # Связь с магазином

    def __str__(self):
        return f"{self.full_name} ({self.phone})"



# Create your models here.
