from django.test import TestCase
from ..models import Book, Author
from ..forms import AuthorForm,BookForm


class AuthorFormTestCase(TestCase):
    def setUp(self) -> None:
        data = {'name':'admin'}
        self.form = AuthorForm(data=data)

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())
        author = self.form.save()
        self.assertTrue(self.form.save())
        self.assertEqual(author.name, 'admin')
        self.assertLessEqual(len(author.name), 100)

    def test_blak_data(self):
        form = AuthorForm()
        self.assertFalse(form.is_valid())
        self.assertEqual(form.fields['name'].required, True)


class BookFormTestCase(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name='admin')
    
    def test_instance_author(self):
        self.assertIsInstance(self.author, Author)
    
    def test_create_form(self):
        self.data = {'name':'admin', 'pricce':12, 'author':self.author}
        form = BookForm(data=self.data)
        self.assertTrue(form.save())
        self.assertEqual(len(form.fields), 3)

    def test_fields_form(self):
        form = BookForm()
        self.assertTrue(form.fields['name'].required, True)
        self.assertNotEqual(len(form.fields), 4)
        self.assertNotIn(form.fields['name'], form)
        book = form.save(commit=False)
        self.assertNotIn(book.name, form)
