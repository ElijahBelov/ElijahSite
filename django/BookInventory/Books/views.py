import re
import csv

from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-pub_date")[:4]
    context = {"book_list":books}

    return render(request, "index.html", context)

def home(request):
    return redirect("index")

def new_book(request):
    if request.method == 'GET':
        return render(request, 'new_book.html')
    elif request.method == 'POST':
        context = {}
        # Check if user exists
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        pub_date = request.POST['pub_date']
        isbn = request.POST['isbn']
        context['form_data'] = {"title": title, "author":author, "genre":genre, "pub_date":pub_date, "isbn":isbn}
        
        def valid_isbn(s):
            s = s.replace("-", "").replace(" ", "").upper();
            if len(s) == 9:
                s = "0" + s
            match = re.search(r'^(\d{9})(\d|X)$', s)
            if not match:
                return False

            digits = match.group(1)
            check_digit = 10 if match.group(2) == 'X' else int(match.group(2))

            result = sum((i + 1) * int(digit) for i, digit in enumerate(digits))
            return (result % 11) == check_digit


        if isbn and not valid_isbn(isbn):
            context['message'] = "Invalid ISBN."
            return render(request, "new_book.html", context)

        book_exist = False
        try:
            Book.objects.get(title=title, author=author)
            book_exist = True
        except:
            pass
        if not book_exist:
            book = Book.objects.create(title=title, author=author, genre=genre, pub_date=pub_date, isbn=isbn)
        else:
            context['message'] = "Book already exists."
            return render(request, "new_book.html", context)
        nav = request.POST.get('submit')
        print(nav)
        if nav == "go_home":
            return HttpResponseRedirect("/index")
        if nav == "see_all":
            return HttpResponseRedirect("/books")
    return render(request, "new_book.html")

def all_books(request):
    filtered_books = cache.get('filtered_books')
    if not filtered_books:
        filtered_books = Book.objects.all()
        cache.set('filtered_books', filtered_books)
    if request.method == 'GET':
        books = Book.objects.all()
        context = {"all_books":books}
        cache.set('filtered_books', books)
        return render(request, "all_books.html", context)
    elif request.method == 'POST':
        books = Book.objects.all()
        title_filter = request.POST['title_filter']
        if title_filter:
            books = books.filter(title__contains=title_filter)
        author_filter = request.POST['author_filter']
        if author_filter:
            books = books.filter(author__contains=author_filter)
        genre_filter = request.POST['genre_filter']
        if genre_filter:
            books = books.filter(genre__contains=genre_filter)
        start_date = request.POST['start_date']
        if start_date:
            books = books.filter(pub_date__gt=start_date)
        end_date = request.POST['end_date']
        if end_date:
            books = books.filter(pub_date__lt=end_date)
        
        cache.set('filtered_books', books)
        context = {"all_books":books}
        context['filter_data'] = {"title": title_filter, "author":author_filter, "genre":genre_filter, "start_date":start_date, "end_date":end_date,}
        return render(request, "all_books.html", context)
        
def download(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(["Entry ID", "Title", "Author", "Genre", "Publication Date", "ISBN"])
    books = cache.get("filtered_books")
    if not books:
        books = Book.objects.all()
    for book in books:
        writer.writerow([book.entry_id, book.title, book.author, book.genre, book.pub_date, book.isbn])

    return response