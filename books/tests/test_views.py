from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from books.models import Book, Comment, ReplyToComment
from books.views import BookListView, book_detail_view


class TestViews(TestCase):
    USERNAME = 'my_username'
    PASSWORD = 'my_password'
    EMAIL = 'myemail@gmail.com'

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username=self.USERNAME, password=self.PASSWORD, email=self.EMAIL)
        self.book1 = Book.objects.create(title='book1', description='Hello', price=12.00, slug='book-1')

        self.list_url = reverse('books_list')
        self.detail_url = reverse('book_detail', kwargs={'slug': self.book1.slug})
        self.create_url = reverse('book_create')

        self.factory = RequestFactory()

    def test_books_list_GET_with_valid_user(self):
        request = self.factory.get(self.list_url)
        request.user = self.user
        response = BookListView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed('books/books_list.html'):
            response.render()
        
    def test_books_list_GET_with_anonymous_user(self):
        request = self.factory.get(self.list_url)
        request.user = AnonymousUser()
        response = BookListView.as_view()(request)

        self.assertEqual(response.status_code, 302)

    def test_book_not_found_error(self):                   # why this func raise error while testing ???
        request = self.factory.get('/books/some-slug/')
        request.user = self.user
        response = book_detail_view(request, 'some-slug')

        self.assertEqual(response.status_code, 404)

    def test_book_detail_GET_with_valid_user(self):
        request = self.factory.get(self.detail_url)
        request.user = self.user
        response = book_detail_view(request, self.book1.slug)

        self.assertEqual(response.status_code, 200)

    def test_book_detail_GET_with_anonymous_user(self):
        request = self.factory.get(self.detail_url)
        request.user = AnonymousUser()
        response = book_detail_view(request, self.book1.slug)

        self.assertEqual(response.status_code, 302)

    def test_book_create_POST(self):
        response = self.client.post(self.create_url, {
            'title': 'book2',
            'description': 'Hi',
            'price': 14.00,
            'slug': 'book-2',
        })
        book2 = Book.objects.get(pk=2)

        self.assertEqual(response.status_code, 302)

        self.assertEqual(book2.title, 'book2')
        self.assertEqual(book2.description, 'Hi')
        self.assertEqual(book2.price, 14.00)
        self.assertEqual(book2.slug, 'book2')
