from django.urls import path

from ToDoApp.api_auth.views import CreateUserApiView

urlpatterns = (
    path('register/', CreateUserApiView.as_view(), name='api register user'),
)
