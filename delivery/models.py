from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from shop.models import Shop

class Courier(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="ФИО курьера",
        validators=[
            MinLengthValidator(5, message="ФИО должно содержать минимум 5 символов")
        ],
        help_text="Введите полное имя курьера"
    )

    phone = models.CharField(
        max_length=13,
        verbose_name="Телефон",
        validators=[
            RegexValidator(
                regex=r'^\+996\d{9}$',
                message="Телефон должен начинаться с +996 и содержать 9 цифр после"
            )
        ],
        help_text="Формат: +996XXXXXXXXX"
    )

    is_active = models.BooleanField(default=True, verbose_name="Активен")

    delivery_zone = models.CharField(
        max_length=100,
        verbose_name="Зона доставки",
        validators=[
            MinLengthValidator(3, message="Зона доставки должна содержать минимум 3 символа")
        ],
        help_text="Например: Южный район, Центр и т.д."
    )

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='couriers',
        verbose_name="Магазин"
    )

    def __str__(self):
        return f"{self.full_name} ({self.phone})"
