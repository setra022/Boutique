from django.contrib import admin

from .models import Article, Product

admin.site.register(Product)
admin.site.register(Article)
