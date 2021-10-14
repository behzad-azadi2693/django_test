from django.http import response
from django.test import TestCase
from ..models import Author, Book
from django.urls import reverse

class ViewBookTestCase(TestCase):
    def setUp(self) -> None:
        for author in range(5):
            author = Author.objects.create(name=f'admin{author}')
            Book.objects.create(name='admin',pricce=12,author=author)

    def test_detail(self):
        author = Author.objects.create(name='admin')
        book = Book.objects.create(name='admin',pricce=15, author=author)
        response = self.client.get(book.get_absolute_url())
        #response = self.client.get(reverse('detail', args=[book.pk]))
        self.assertTemplateUsed(response, 'detail.html')
        self.assertTrue(response.context['book'])
        
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_len_books(self):
        response = self.client.get('/')    
        self.assertGreaterEqual(len(response.context['books']), 4)
        self.assertEqual(len(response.context['books']), 5)