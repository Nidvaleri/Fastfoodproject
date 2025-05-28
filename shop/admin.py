from django.contrib import admin
from .models import Category, Product, Discount, Combo, Cart, CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Combo)
admin.site.register(Cart)
admin.site.register(CartItem)



# Register your models here.
