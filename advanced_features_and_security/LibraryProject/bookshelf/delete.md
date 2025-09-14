from bookshelf.models import Book

["book.delete"]

b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()

Book.objects.all()

