from rest_framework import generics, viewsets, permissions
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    querysets = Book.objects.all()
    serializer = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    querysets = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action=='destroy':
            return [permissions.IsAdminUser()]
        elif self.action in ['create', 'update']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# Create your views here.
