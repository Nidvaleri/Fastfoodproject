from django.contrib import admin
from django.contrib import admin
from .models import Category, Product, Discount, Combo, Cart, CartItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')          # Показываем в списке id и имя категории
    search_fields = ('name',)               # Поиск по названию категории

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'weight', 'quantity')
    list_filter = ('category',)             # Фильтр по категории справа
    search_fields = ('name',)               # Поиск по названию товара

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage')
    search_fields = ('name',)

class ComboAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    filter_horizontal = ('products',)      # Удобный мультиселект для продуктов в комбо

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'created_at')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')

# Регистрируем модели в админке
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Combo, ComboAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)


# Register your models here.
