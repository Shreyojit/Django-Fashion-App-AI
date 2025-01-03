from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models, serializers
from notification.models import Notification
from core.models import Product
from extras.models import Address
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Create your views here.

class AddOrder(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        print("Received request data: ", data)  # Debug: print the received data
        
        try:
            with transaction.atomic():
                validated_products = []
                
                # Validate the order products
                for product_data in data['order_products']:
                    product = get_object_or_404(Product, id=product_data['product'])
                    print(f"Validating product with id {product.id}")  # Debug: print the product being validated
                    
                    validated_products.append(
                        {
                            "product_id": product.id,
                            "imageUrl": product.imageUrls,
                            "title": product.title,
                            "price": product.price,
                            "quantity": product_data['quantity'],
                            "size": product_data['size'],
                            "color": product_data['color'],
                        }
                    )
                
                # Get the address
                address = get_object_or_404(Address, id=int(data['address']))
                print(f"Address retrieved: {address}")  # Debug: print the address
                
                # Create the order
                order = models.Order.objects.create(
                    user=request.user,
                    customer_id=data["customer_id"],
                    address=address,
                    order_products=validated_products,
                    rated=[0],
                    total_quantity=data['total_quantity'],
                    subtotal=data['subtotal'],
                    total=data['total'],
                    delivery_status=data.get('delivery_status', models.Order.PENDING),
                    payment_status=data.get('payment_status', models.Order.UNPAID)
                )
                print(f"Order created with ID: {order.id}")  # Debug: print the created order ID
                
                # Create a notification for the user
                title = "Order Successfully Placed"
                message = "Your payment has been successfully processed, and your order is now in progress."
                print(f"Creating notification for order ID: {order.id} with message: {message}")  # Debug: print the notification data
                print(order)
                notification = Notification.objects.create(
                    orderId=order,
                    title=title,
                    message=message,
                    userId=request.user
                )
                print(f"Notification created with ID: {notification.id}")  # Debug: print the created notification ID
                print(notification)
                order.save()
                print("Order saved successfully.")  # Debug: confirm order save
                
                return Response({"id": order.id}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(f"Error occurred: {str(e)}")  # Debug: print any error messages
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserOrderByStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve status from query parameters
        order_status = request.query_params.get('status', None)

        # Get the orders based on status and order them by created_at descending
        if order_status:
            orders = models.Order.objects.filter(user=request.user, delivery_status=order_status).order_by('-created_at')
        else:
            # If no status provided, return all orders for the user
            orders = models.Order.objects.filter(user=request.user).order_by('-created_at')

        # Serialize the order data
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve order_id from query parameters using query_params.get()
        order_id = request.query_params.get('id', None)
        
        if not order_id:
            return Response({"error": "Order ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the order by ID and ensure it's the authenticated user's order
            order = models.Order.objects.get(id=order_id, user=request.user)
        except models.Order.DoesNotExist:
            return Response({"error": "Order not found or not authorized to view this order"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the order data
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
