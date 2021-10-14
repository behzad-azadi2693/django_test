from django.urls import path
from .views import index, detail

urlpatterns = [ 
    path('', index),
    path('book_detail/<int:pk>/', detail, name='detail')
]