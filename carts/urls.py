from django.urls import path
from .views import AddItemToCart, RemoveItemFromCart, CartCount, UpdateCartItemQuantity, GetUserCart

urlpatterns = [
    path('add/', AddItemToCart.as_view(), name='add_item_to_cart'),
    path('delete/', RemoveItemFromCart.as_view(), name='remove_item_from_cart'),
    path('count/', CartCount.as_view(), name='cart_count'),
    path('update/', UpdateCartItemQuantity.as_view(), name='update_cart_item_quantity'),
    path('me/', GetUserCart.as_view(), name='get_user_cart'),
]
