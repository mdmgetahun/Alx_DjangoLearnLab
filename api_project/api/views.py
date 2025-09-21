from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    querysets = Book.objects.all()
    serializer = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    querysets = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
