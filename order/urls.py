from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.UserOrderByStatus.as_view(), name='user-order-by-status'),
    path('details/', views.OrderDetails.as_view(), name='order-details'),
    path('add/', views.AddOrder.as_view(), name='add-order'),
]
