from django.urls import path
from . import views

urlpatterns = [
    # Add a new address
    path('add/', views.AddAddress.as_view(), name='add-address'),
    
    # Get all addresses of the logged-in user
    path('addresslist/', views.GetUserAddress.as_view(), name='get-user-address'),
    
    # Get the default address of the logged-in user
    path('default/', views.GetDefaultAddress.as_view(), name='get-default-address'),
    
    # Delete an address by ID
    path('delete/', views.DeleteAddress.as_view(), name='delete-address'),
    
    # Set an address as the default address
    path('default/', views.SetDefaultAddress.as_view(), name='set-default-address'),
]
