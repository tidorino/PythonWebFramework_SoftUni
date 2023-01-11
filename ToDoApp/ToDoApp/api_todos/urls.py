from django.urls import path

from ToDoApp.api_todos.views import ListCreateTodoApiView, ListCategoriesApiView, DetailsTodoApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name='api list todo'),
    path('<int:pk>/', DetailsTodoApiView.as_view(), name='api details todo'),
    path('categories/', ListCategoriesApiView.as_view(), name='api list categories'),
)
