from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Address
from .serializers import AddressSerializer


# Add a new Address
class AddAddress(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        data['userId'] = user.id  # Assign the logged-in user to the address

        # Create a new address
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            address = serializer.save()
            return Response({"message": "Address added successfully", "address": AddressSerializer(address).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all addresses of the logged-in user
class GetUserAddress(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        addresses = Address.objects.filter(userId=user)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Get the default address of the logged-in user
class GetDefaultAddress(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            address = Address.objects.get(userId=user, isDefault=True)
            serializer = AddressSerializer(address)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Address.DoesNotExist:
            return Response({"message": "No default address found"}, status=status.HTTP_404_NOT_FOUND)


# Delete an address by ID (using query parameters)
class DeleteAddress(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        address_id = request.query_params.get('id')  # Retrieve the address ID from query parameters

        if not address_id:
            return Response({"message": "Address ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            address = Address.objects.get(id=address_id, userId=user)
            address.delete()
            return Response({"message": "Address deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Address.DoesNotExist:
            return Response({"message": "Address not found"}, status=status.HTTP_404_NOT_FOUND)


# Set an address as the default address (using query parameters)
class SetDefaultAddress(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        address_id = request.query_params.get('id')  # Retrieve the address ID from query parameters

        if not address_id:
            return Response({"message": "Address ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            address = Address.objects.get(id=address_id, userId=user)

            # Set all other addresses to not default
            Address.objects.filter(userId=user).update(isDefault=False)

            # Set the selected address as default
            address.isDefault = True
            address.save()
            return Response({"message": "Address set as default successfully"}, status=status.HTTP_200_OK)

        except Address.DoesNotExist:
            return Response({"message": "Address not found"}, status=status.HTTP_404_NOT_FOUND)
