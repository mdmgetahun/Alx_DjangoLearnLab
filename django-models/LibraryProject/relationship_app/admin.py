from django.contrib import admin

from .models import Author
from .models import Book
from .models import Library
from .models import Librarian

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name",)
    search_fields = ("name",) 
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)
    list_filter = ("title", "author",)
    search_fields = ("title", "author",)
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name", )
    search_filter = ("name", )

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("name", "library",)
    list_filter = ("name", "library",)
    search_filter = ("name", "library")



