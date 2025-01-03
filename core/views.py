from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . import models, serializers
import random
from rest_framework.views import APIView


# Category List View
class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

# Home Category List View (Random order of 5 categories)
class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        # Get all categories and shuffle them
        queryset = models.Category.objects.all()
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:5]

# Brand List View
class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer
    queryset = models.Brand.objects.all()

# Product List View (Random order of 20 products)
class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        # Get all products and shuffle them
        queryset = models.Product.objects.all()
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]

# Popular Products List View (Filter products with ratings between 4.0 and 5.0)
class PopularProductsList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer  # Assuming ProductSerializer is used for response

    def get_queryset(self):
        # Filter products with ratings between 4.0 and 5.0
        queryset = models.Product.objects.filter(
            rating__gte=4.0, rating__lte=5.0
        )
        # Shuffle the queryset to get random products from the filtered list
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]

# Product List by Clothes Type (Filter products based on clothes type)
class ProductListByClothesType(APIView):
    
    def get(self, request):
        # Get 'clothesType' from query parameters
        query = request.query_params.get('clothesType', None)

        if query:
            # Filter products by the provided clothesType
            products = models.Product.objects.filter(clothesType=query)
            
            # Shuffle the queryset for randomness
            product_list = list(products)
            random.shuffle(product_list)
            
            # Return the first 20 results
            limited_products = product_list[:20]
            
            # Serialize the products and return the response
            serializer = serializers.ProductSerializer(limited_products, many=True)
            return Response(serializer.data)
        
        else:
            # If no clothesType is provided, return a bad request response
            return Response(
                {'message': 'No clothesType query parameter provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class SimilarProducts(APIView):
    
    def get(self,request):
       query = request.query_params.get('category',None)
    
       if query:
            products = models.Product.objects.filter(category=query)
            
            product_list = list(products)
            random.shuffle(product_list)
            
            limited_products = product_list[:6]
            
            serializer = serializers.ProductSerializer(limited_products,many=True)
            
            return Response(serializer.data)    
       else:
           return Response({'message':'No query provided'},
                           status=status.HTTP_400_BAD_REQUEST,
                           )
           
class SearchProductByTitle(APIView):
    
    def get(self, request):
        # Get 'title' from query parameters
        title_query = request.query_params.get('title', None)

        if title_query:
            # Filter products by the provided title
            products = models.Product.objects.filter(title__icontains=title_query)
            
            # Shuffle the queryset for randomness
            product_list = list(products)
            random.shuffle(product_list)
            
            # Return the first 20 results
            limited_products = product_list[:20]
            
            # Serialize the products and return the response
            serializer = serializers.ProductSerializer(limited_products, many=True)
            return Response(serializer.data)
        
        else:
            # If no title is provided, return a bad request response
            return Response(
                {'message': 'No title query parameter provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class FilterProductByCategory(APIView):
    
    def get(self, request):
        # Get 'category' from query parameters
        category_query = request.query_params.get('category', None)

        if category_query:
            # Filter products by the provided category
            products = models.Product.objects.filter(category__title__icontains=category_query)
            
            # Shuffle the queryset for randomness
            product_list = list(products)
            random.shuffle(product_list)
            
            # Return the first 20 results
            limited_products = product_list[:20]
            
            # Serialize the products and return the response
            serializer = serializers.ProductSerializer(limited_products, many=True)
            return Response(serializer.data)
        
        else:
            # If no category is provided, return a bad request response
            return Response(
                {'message': 'No category query parameter provided'},
                status=status.HTTP_400_BAD_REQUEST
            )            
           