from django.test import SimpleTestCase
from django.urls import reverse, resolve

from books.views import BookListView, BookCreateView, book_detail_view, BookUpdateView, BookDeleteView

class TestUrls(SimpleTestCase):

    def test_books_list_url_resolves(self):
        url = reverse('books_list')
        self.assertEqual(resolve(url).func.view_class, BookListView)

    def test_book_create_url_resolves(self):
        url = reverse('book_create')
        self.assertEqual(resolve(url).func.view_class, BookCreateView)
     
    def test_book_detail_url_resolves(self):
        url = reverse('book_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func, book_detail_view)
        
    def test_book_update_url_resolves(self):
        url = reverse('book_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, BookUpdateView)

    def test_book_delete_url_resolves(self):
        url = reverse('book_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, BookDeleteView)
