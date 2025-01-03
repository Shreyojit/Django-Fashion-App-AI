from django.db import models
from django.contrib.auth.models import User
from extras.models import Address

# Create your models here.

class Order(models.Model):
    PENDING = 'pending'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

    ORDERSTATUS = (
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )

    PAID = 'paid'
    UNPAID = 'unpaid'
    CASH_ON_DELIVERY = 'cash_on_delivery'
    CARD = 'card'
    UPI = 'upi'
    FAILED = 'failed'  # New option for failed payment

    PAYMENTSTATUS = (
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (CASH_ON_DELIVERY, 'Cash on Delivery'),
        (CARD, 'Card'),
        (UPI, 'UPI'),
        (FAILED, 'Failed'),  # Add 'Failed' to the options
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user who placed the order
    customer_id = models.CharField(max_length=100)  # Customer ID, can be a string
    address = models.ForeignKey(Address, on_delete=models.CASCADE)  # Reference to the address where the order is delivered
    order_products = models.JSONField(default=list)  # List of products in the order (stored as JSON)
    rated = models.JSONField(default=list)  # List to store product ratings (stored as JSON)
    total_quantity = models.IntegerField()  # Total quantity of products in the order
    subtotal = models.FloatField()  # Subtotal amount for the products before taxes and delivery
    total = models.FloatField()  # Total amount after adding taxes and delivery fees
    delivery_status = models.CharField(max_length=20, choices=ORDERSTATUS, default=PENDING)  # Current delivery status
    payment_status = models.CharField(max_length=20, choices=PAYMENTSTATUS, default=UNPAID)  # Current payment status
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the order is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when the order is updated

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - Payment Status: {self.payment_status}, Delivery Status: {self.delivery_status}"
