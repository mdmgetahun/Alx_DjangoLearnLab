from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    querysets = Book.objects.all()
    serializer = BookSerializer
# Create your views here.
