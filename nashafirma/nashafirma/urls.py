from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls  #doc swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/orders/', include('orders.urls')),
    path('api/items/', include('items.urls')),
    path('api/products/', include('products.urls')),
]

urlpatterns += doc_urls
