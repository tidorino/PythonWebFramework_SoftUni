from django.urls import path

from BooksRestProject.books_api.views import ListBookApiView, DetailBookApiView

urlpatterns = (
    path('books/', ListBookApiView.as_view(), name='List books'),
    path('books/<int:pk>/', DetailBookApiView.as_view(), name='Details book')
)
