from django.contrib import admin

from BooksRestProject.books_api.models import Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'author',)

