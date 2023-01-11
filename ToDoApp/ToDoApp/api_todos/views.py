from rest_framework.generics import ListCreateAPIView, ListAPIView

from ToDoApp.api_todos.models import Todo, Category
from ToDoApp.api_todos.serializers import TodoSerializer, CategorySerializer


class ListCreateTodoApiView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListCategoriesApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
