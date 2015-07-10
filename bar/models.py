from django.db import models
from django.contrib.auth import models as user_models

# Create your models here.

class Product(models.Model):
    PRODUCT_TYPES = (
        ('S', 'Snack'),
        ('D', 'Drink'),
        ('A', 'Alcoholic Beverage')
    )

    name = models.TextField()
    description = models.TextField()
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    product_price = models.DecimalField(decimal_places=2, max_digits=6)


class Sale(models.Model):
    product_sold = models.ForeignKey(Product)
    datetime_sold = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(user_models.User)

