from django.contrib import admin

from .models import Article, Cart, CartOrder, Product

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Cart)
admin.site.register(CartOrder)
