from django.urls import path

from ToDoApp.api_auth.views import CreateUserApiView, LoginApiView, LogoutApiView

urlpatterns = (
    path('register/', CreateUserApiView.as_view(), name='api register user'),
    path('login/', LoginApiView.as_view(), name='api login user'),
    path('logout/', LogoutApiView.as_view(), name='api logout user'),
)
