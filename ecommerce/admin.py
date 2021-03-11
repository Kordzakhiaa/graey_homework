from django.contrib import admin

from ecommerce.models import Product, Category, Cart, CartItem, Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Tag)
