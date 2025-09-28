from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path, include

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'), #List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'), #path to get details of a specific book
    path('books/create/', BookCreateView.as_view(), name='book_create'), #path to create a new book
    path('books/update/', BookUpdateView.as_view(), name='book_update'), #path to update a specific book
    path('books/delete/', BookDeleteView.as_view(), name='book_delete'),#path to delete a specific book

]