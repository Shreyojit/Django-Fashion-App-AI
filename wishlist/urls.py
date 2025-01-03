from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.GetWishList.as_view(), name='get_wishlist'),  # URL for fetching the wishlist
    path('toggle/', views.ToggleWishList.as_view(), name='toggle_wishlist'),  # URL for toggling wishlist items
]
