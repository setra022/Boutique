from django.db import models

from shop.settings import AUTH_USER_MODEL
    

class Article(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.article.name} ({self.size})'
    

class Cart(models.Model):
    customer = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer} cart'
    
    def add(self, product):
        cartorder, _ = self.cartorder_set.get_or_create(product=product)
        cartorder.amount += 1
        cartorder.save()
    

class CartOrder(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.cart} - {self.product} ({self.amount})'