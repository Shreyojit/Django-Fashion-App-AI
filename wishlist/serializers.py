from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class WishListSerializer(serializers.ModelSerializer):
    # Referencing related Product model fields
    title = serializers.ReadOnlyField(source="product.title")  
    description = serializers.ReadOnlyField(source="product.description")
    is_featured = serializers.ReadOnlyField(source="product.is_featured")
    clothesType = serializers.ReadOnlyField(source="product.clothesType")
    rating = serializers.ReadOnlyField(source="product.rating")
    category = serializers.ReadOnlyField(source="product.category.title")  # Accessing category's title field
    colors = serializers.ReadOnlyField(source="product.colors")
    sizes = serializers.ReadOnlyField(source="product.sizes")
    imageUrls = serializers.ReadOnlyField(source="product.imageUrls")
    created_at = serializers.ReadOnlyField(source="product.created_at")

    # Include userId with username
    userId = serializers.ReadOnlyField(source="userId.username")

    class Meta:
        model = models.WishList
        fields = [
            'id', 'title', 'description', 'is_featured', 'clothesType', 
            'rating', 'category', 'colors', 'sizes', 'imageUrls', 'created_at', 'userId'
        ]
