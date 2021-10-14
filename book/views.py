from django.shortcuts import render
from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.all().order_by('pricce')

    context = {
        'books':books
    }

    return render(request, 'index.html', context)

def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book':book
    }

    return render(request, 'detail.html', context)