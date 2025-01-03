from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from core.serializers import ProductSerializer

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    # User field
    user = serializers.ReadOnlyField(source="userId.username")  # Username of the user

    class Meta:
        model = models.Cart
        exclude = ['userId','created_at','updated_at']
