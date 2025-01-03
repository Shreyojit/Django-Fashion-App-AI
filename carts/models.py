from django.db import models
from django.contrib.auth.models import User
from core.models import Product

# Create your models here.

class Cart(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Reference to the product
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the cart
    size = models.CharField(max_length=50, blank=True, null=True)  # Size of the product (if applicable)
    colors = models.CharField(max_length=50, blank=True, null=True)  # Colors of the product (if applicable)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the cart item is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when the cart item is modified

    def __str__(self):
      product_title = self.product.title if self.product else 'No Product'
      return "{}/{} (Qty: {})".format(self.userId.username, product_title, self.quantity)
