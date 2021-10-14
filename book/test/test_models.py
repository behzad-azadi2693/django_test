from django.test import TestCase
from ..models import Book, Author

class BookTestCase(TestCase):
    
    def creat_book(self, name='admin'):
        author = Author.objects.create(name=name)
        return Book.objects.create(name='admin', pricce=13, author=author)

    def test_book_model(self):
        book = self.creat_book()
        self.assertEqual(book.name, book.__str__())
        self.assertEqual(book.name, str(book))
        self.assertTrue(isinstance(book, Book))
    
    def test_verbose_name_plural(self):
        self.assertEqual(str(Book._meta.verbose_name_plural), "books")

    def test_verbose_name(self):
        book = self.creat_book()
        self.assertEqual(book._meta.get_field('name').verbose_name, 'book name')

class AuthorTestCase(TestCase):
    
    def setUp(self, name='admin'):
        Author.objects.create(name=name)

    def test_author_model(self):
        author = Author.objects.get(name='admin')
        authors = Author.objects.all()
        self.assertIn(author,authors)
        self.assertEqual(author.name, 'admin')
        self.assertIsInstance(author, Author)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Author._meta.verbose_name_plural), "authors")
