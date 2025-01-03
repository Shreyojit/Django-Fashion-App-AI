from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'imageUrl']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title', 'imageUrl']

class ProductSerializer(serializers.ModelSerializer):
      # Use PrimaryKeyRelatedField for category and brand to show only the ID
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    
    class Meta:
        model = Product
        fields = '__all__'
