from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, Product
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Add Item to Cart (already implemented)
class AddItemToCart(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        data = request.data
        
        try:
            product = Product.objects.get(id=data['product'])
        except Product.DoesNotExist:
            return Response(
                {'message': 'Product does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )  

        try:
            cart_item = Cart.objects.get(
                userId=user,
                product=product,
                color=data['color'],
                size=data['size']
            )  

            cart_item.quantity += data.get('quantity', 1)
            cart_item.save()
            return Response(
                {'message': 'Item updated successfully'},
                status=status.HTTP_200_OK
            )
        except Cart.DoesNotExist:
            Cart.objects.create(
                userId=user,
                product=product,
                color=data['color'],
                size=data['size'],
                quantity=data.get('quantity', 1),
            )
            return Response(
                {'message': 'Item added successfully'},
                status=status.HTTP_201_CREATED
            )


# Remove Item from Cart
class RemoveItemFromCart(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        user = request.user
        data = request.data
        
        product = get_object_or_404(Product, id=data['product'])
        size = data.get('size')
        color = data.get('color')
        
        try:
            cart_item = Cart.objects.get(
                userId=user,
                product=product,
                size=size,
                color=color
            )
            cart_item.delete()
            return Response({'message': 'Item removed from cart successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({'message': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)


# Cart Count (Number of items in user's cart)
class CartCount(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        cart_items = Cart.objects.filter(userId=user)
        total_items = sum(item.quantity for item in cart_items)
        return Response({"total_items": total_items}, status=status.HTTP_200_OK)


# Update Cart Item Quantity
class UpdateCartItemQuantity(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        user = request.user
        data = request.data
        
        product = get_object_or_404(Product, id=data['product'])
        size = data.get('size')
        color = data.get('color')
        quantity = data.get('quantity')

        if quantity <= 0:
            return Response({"detail": "Quantity must be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = Cart.objects.get(
                userId=user,
                product=product,
                size=size,
                color=color
            )
            cart_item.quantity = quantity
            cart_item.save()
            return Response(CartSerializer(cart_item).data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"message": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)


# Get User Cart
class GetUserCart(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        cart_items = Cart.objects.filter(userId=user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
