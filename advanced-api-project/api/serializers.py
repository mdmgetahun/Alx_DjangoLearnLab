from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#Serializer for the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = '__all__'

    #validates to check inserted date is not in the future

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year can't be in the future.")
        return value
    
#Serializer for the author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta():
        model = Author
        fields = '__all__'
