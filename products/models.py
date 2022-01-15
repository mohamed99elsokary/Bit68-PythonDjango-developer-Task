from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    # relations
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_seller"
    )
    # fields
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name
