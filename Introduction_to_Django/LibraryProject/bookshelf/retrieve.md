from bookshelf.models import Book

books = Book.objects.all()
books

b = books[0]
b.title, b.author, b.publication_year

