from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name