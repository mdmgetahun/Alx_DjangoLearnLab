from bookshelf.models import Book

books = Book.objects.all()
books

["Book.objects.get", "1984"]

b = books[0]
b.title, b.author, b.publication_year

