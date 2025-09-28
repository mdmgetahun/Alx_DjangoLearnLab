from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework import permissions

class BookListView(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #Anyone can view the list of books


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #Anyone can view the details of a book

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()   
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #Only authenticated users can create books

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]    #Only authenticated users can update books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_classs = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  #Only authenticated users can delete books
# Create your views here.
