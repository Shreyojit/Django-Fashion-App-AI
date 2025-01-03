from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
    path('api/products/', include('core.urls')),  # Add trailing slash here
    path('api/wishlist/',include('wishlist.urls')),
    path('api/cart/',include('carts.urls')),
    path('api/address/',include('extras.urls'))
]
