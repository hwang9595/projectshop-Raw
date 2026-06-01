from django.db import models


class Shop(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_price = models.FloatField()
    Product_count = models.IntegerField()
    Product_available = models.BooleanField()
    Product_str = models.CharField(max_length=100)

# Create your models here.
