from rest_framework import serializers
from .models import Notification  # Ensure the correct import path for Notification model

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'  # Automatically include all fields from the Notification model
