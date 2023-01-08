from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ToDoApp.api_auth.urls')),
    path('auth/', include('ToDoApp.api_todos.urls')),
]
