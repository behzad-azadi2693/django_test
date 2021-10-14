from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='book name')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pricce = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])
    