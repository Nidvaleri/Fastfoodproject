from django.db import models

# Категории товаров
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Продукты
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.PositiveIntegerField(help_text="Вес в граммах")
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name

# Скидки
class Discount(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(help_text="Скидка в процентах")  # например: 10
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"

# Комбо-наборы
class Combo(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# Корзина клиента
class Cart(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id} for {self.client}"

# Позиции в корзине
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# Create your models here.
