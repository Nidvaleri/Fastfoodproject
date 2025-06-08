# models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название магазина")
    address = models.TextField(blank=True, verbose_name="Адрес магазина")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(0.01, message="Цена должна быть больше нуля")]
    )
    weight = models.PositiveIntegerField(
        help_text="Вес в граммах",
        validators=[MinValueValidator(1, message="Вес должен быть больше нуля")]
    )
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв на {self.product.name} от {self.author_name}"


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(
        help_text="Скидка в процентах",
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"


class Combo(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(0.01, message="Цена должна быть больше нуля")]
    )

    def __str__(self):
        return self.name


class Cart(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина #{self.id} клиента {self.client.name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='shop_cartitems')
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1, message="Количество должно быть не меньше 1")]
    )

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
