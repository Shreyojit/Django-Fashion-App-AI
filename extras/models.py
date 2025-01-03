from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    HOME = "home"
    OFFICE = "office"
    SCHOOL = "school"
    ADRESSTYPES = {
        (HOME, "Home"),
        (OFFICE, "Office"),
        (SCHOOL, "School"),
    }
    
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Latitude
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Longitude
    isDefault = models.BooleanField(default=False)  # Whether the address is the default address
    address = models.CharField(max_length=255)  # The address line
    phone = models.CharField(max_length=20)  # The phone number for this address
    userId = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user
    addressType = models.CharField(
        max_length=10, 
        choices=ADRESSTYPES, 
        default=HOME
    )  # Type of address (Home, Office, School)

    def __str__(self):
        return f"{self.userId.username} - {self.addressType} - {self.address}"


class Extras(models.Model):
    isVerified = models.BooleanField(default=False)  # Whether the user's extra information is verified
    otp = models.CharField(max_length=6, blank=True, null=True)  # One-time password for verification
    userId = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user

    def __str__(self):
        return f"Extra info for {self.userId.username} - Verified: {self.isVerified}"
