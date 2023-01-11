from django.urls import path

from ToDoApp.api_todos.views import ListCreateTodoApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name='api list todo'),
)
