from django.contrib import admin

from .models import Author
from .models import Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    list_filter = ("name",)
    search_fields = ("name","birth_date")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")

# Register your models here.
