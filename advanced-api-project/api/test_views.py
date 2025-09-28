from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # create an author
        self.author = Author.objects.create(name='Myles Munroe')
        
        # create a book
        self.book = Book.objects.create(
            title='The Power of Vision',
            author=self.author,
            publication_year=2001
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)  # make sure it returns at least 1 book

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Power of Vision')
    
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2025
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'The Power of Vision Updated'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'The Power of Vision Updated')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_by_title(self):
        url = reverse('book-list') + '?title=The Power of Vision'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    def test_search_title(self):
        url = reverse('book-list') + '?search=Vision'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    def test_ordering(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['title'], 'The Power of Vision')
