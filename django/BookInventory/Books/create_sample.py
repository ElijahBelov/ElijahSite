from models import Book
from django.conf import settings

settings.configure(DEBUG=True)
book = Book.objects.create_book()
