from django.db import models

__all__ = (
    'Place',
    'Restaurant',
)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serve_pizza = models.BooleanField(default=False)

class Supplier(Place):
    customers = models.ManyToManyField(
        Place,
        related_name='providers',
        related_query_name='provider'
    )