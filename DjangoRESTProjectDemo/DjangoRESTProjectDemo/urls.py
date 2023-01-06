from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Enables browsable API
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('DjangoRESTProjectDemo.api_web.urls')),
]
