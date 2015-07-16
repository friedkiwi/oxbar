from django.db import models
from django.contrib.auth import models as user_models

# Create your models here.


class Product(models.Model):
    PRODUCT_TYPES = (
        ('S', 'Snack'),
        ('D', 'Drink'),
        ('A', 'Alcoholic Beverage')
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    product_price = models.DecimalField(decimal_places=2, max_digits=6)
    is_vegan = models.BooleanField(verbose_name='Vegan ?', default=False)
    is_vegetarian = models.BooleanField(verbose_name='Vegetarian ?', default=False)
    contains_nuts = models.BooleanField(verbose_name='Nuts ?', default=False)
    contains_milk = models.BooleanField(verbose_name='Milk ?', default=False)
    sold_tracker = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product_sold = models.ForeignKey(Product)
    datetime_sold = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(user_models.User)

