from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("entry_id")[:10]
    context = {"book_list":books}

    return render(request, "index.html", context)

def home(request):
    return redirect("index")
