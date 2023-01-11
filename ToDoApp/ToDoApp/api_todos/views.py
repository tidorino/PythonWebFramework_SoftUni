from rest_framework import permissions, exceptions as rest_exceptions
from rest_framework import generics as rest_generic_views

from ToDoApp.api_todos.models import Todo, Category
from ToDoApp.api_todos.serializers import CategorySerializer, TodoForListSerializer, \
    TodoForCreateSerializer, TodoForDetailsSerializer


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    list_serializer_class = TodoForListSerializer
    create_serializer_class = TodoForCreateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class DetailsTodoApiView(rest_generic_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoForDetailsSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        todo = super().get_object()
        if todo.user != self.request.user:
            raise rest_exceptions.PermissionDenied
        return todo


class ListCategoriesApiView(rest_generic_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
