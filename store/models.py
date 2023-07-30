from django.db import models

# Create your models here.
    

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
