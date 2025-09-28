from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework import permissions, IsAuthenticated, IsAuthenticatedOrReadOnly, filters

class BookListView(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #Anyone can view the list of books

   def get_queryset(self):
        queryset = Book.objects.all()
        #Filter by author
        author_id = self.request.query_params.get('author')
        if author_id:
            queryset = queryset.filter(author__id=author_id)

        #Filter by published year
        published_year = self.request.query_params.get('published_year')
        if published_year:
            queryset = queryset.filter(published_year=published_year)
        return queryset


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
