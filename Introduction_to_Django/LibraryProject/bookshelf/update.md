from bookshelf.models import Book

["book.title"]

b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()

b.title

