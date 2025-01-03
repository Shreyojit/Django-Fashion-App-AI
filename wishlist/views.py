from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

# Create your views here.

class GetWishList(generics.ListAPIView):
    serializer_class = serializers.WishListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return models.WishList.objects.filter(userId=self.request.user)


class ToggleWishList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        product_id = request.query_params.get('id')  # Get product ID from query parameters

        if not product_id:
            return Response(
                {'message': 'Invalid request. A product ID is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = models.Product.objects.get(id=product_id)  # Retrieve the product
        except models.Product.DoesNotExist:
            return Response(
                {'message': 'Product not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if the wishlist item exists or create a new one
        wishList_item, created = models.WishList.objects.get_or_create(
            userId=request.user,
            product=product
        )

        if created:
            return Response(
                {'message': 'Product added to wishlist.'},
                status=status.HTTP_201_CREATED
            )
        else:
            wishList_item.delete()
            return Response(
                {'message': 'Product removed from wishlist.'},
                status=status.HTTP_204_NO_CONTENT
            )
