from django.db import models
from django.forms import Form, ModelForm, fields
from .models import Author,Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)
    
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'pricce', 'author')
    