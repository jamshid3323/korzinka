from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as drf_ui_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/version_1/', include('products.urls')),
]

urlpatterns += drf_ui_urls
