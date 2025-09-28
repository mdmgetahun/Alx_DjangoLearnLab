from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework import permissions, filters, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

class BookListView(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #Anyone can view the list of books

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] #filtering
    filterset_fields = ['title', 'author', 'publication_year']
 
    search_fields = ['title', 'author__name'] #searching

    ordering_fields = ['title', 'publication_year'] #ordering
    ordering = ['title']  # default ordering


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #Anyone can view the details of a book

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()   
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] #Only authenticated users can create books

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]    #Only authenticated users can update books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_classs = BookSerializer
    permission_classes = [IsAuthenticated]  #Only authenticated users can delete books
# Create your views here.
