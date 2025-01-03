from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, Extras


# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'



# Extras Serializer
class ExtrasSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Extras
        fields = '__all__'

    
