from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

from .views import BookListView
from .models import Book

class BookListViewTests(TestCase):
    USERNAME = 'User1'
    PASSWORD = 'password'
    EMAIL = 'user1@gmail.com'

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username=cls.USERNAME, password=cls.PASSWORD, email=cls.EMAIL)
        cls.factory = RequestFactory()

        cls.book1 = Book.objects.create(title='title1', description='Hello from book1', price=12.5, slug='title-1')
        cls.book2 = Book.objects.create(title='title2', description='Hello from book2', price=8.6, slug='title-2')

    def test_book_list_view_url_and_template_with_valid_user(self):
        request = self.factory.get(reverse('books_list'))
        request.user = self.user
        response = BookListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'books/books_list.html')
    
    def test_book_list_view_url_with_anonymous_user(self):
        request = self.factory.get(reverse('books_list'))
        request.user = AnonymousUser()
        response = BookListView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_book_list_view_content(self):
        request = self.factory.get(reverse('books_list'))
        request.user = self.user
        response = BookListView.as_view()(request)
        self.assertContains(response, self.book1.title.capitalize())
