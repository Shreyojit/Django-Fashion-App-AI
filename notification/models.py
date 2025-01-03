from django.db import models
from django.contrib.auth.models import User
from order.models import Order  # Assuming Order model is in the same directory, adjust import if necessary

# Create your models here.
class Notification(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)  # Reference to the associated order
    title = models.CharField(max_length=255)  # Title of the notification
    message = models.TextField()  # Message content of the notification
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the notification is created
    isRead = models.BooleanField(default=False)  # Whether the notification has been read
    userId = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user the notification is for
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the notification is last updated

    def __str__(self):
        return "{} | {}".format(self.userId.username, self.userId.id)
