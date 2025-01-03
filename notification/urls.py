from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.NotificationListView.as_view(), name='notification-list'),
    path('count/', views.GetNotificationCount.as_view(), name='notification-count'),
    path('update/', views.UpdateNotificationStatus.as_view(), name='notification-update'),
]
