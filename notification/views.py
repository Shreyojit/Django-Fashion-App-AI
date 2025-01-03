from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(APIView):
    """
    Retrieve all notifications for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(userId=request.user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetNotificationCount(APIView):
    """
    Get the count of unread notifications for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        unread_count = Notification.objects.filter(userId=request.user, isRead=False).count()
        return Response({"unread_count": unread_count}, status=status.HTTP_200_OK)


class UpdateNotificationStatus(APIView):
    """
    Update the status of a notification (mark as read/unread) using query parameter 'id'.
    """
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        notification_id = request.query_params.get('id', None)

        if not notification_id:
            return Response({"error": "Notification ID ('id') is required as a query parameter."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        notification = get_object_or_404(Notification, id=notification_id, userId=request.user)

        # Update the isRead status
        is_read_status = request.data.get("isRead", None)
        if is_read_status is None:
            return Response({"error": "isRead field is required in the request body."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        notification.isRead = is_read_status
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)
