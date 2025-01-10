import os
import re
import csv

from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.static import serve

from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from .logic import profile_pic

from .models import Book

# Create your views here.


def home(request):
	books = Book.objects.all().order_by("-pub_date")[:4]
	context = {"book_list": books}
	return render(request, "index.html", context)

def gohome(request):
	return redirect("home")

def index(request):
	return redirect("home")

def get_profile(request):
	books = Book.objects.all().order_by("-pub_date")[:4]
	context = {"book_list": books}
	context["got_animal"], context["profile_background"] = profile_pic.get_animal(), profile_pic.get_gradient()
	return render(request, "index.html", context) #, context_instance = RequestContext(request)

@login_required
def new_book(request):
	if request.method == "GET":
		return render(request, "new_book.html")
	elif request.method == "POST":
		context = {}
		# Check if user exists
		title = request.POST["title"]
		author = request.POST["author"]
		genre = request.POST["genre"]
		pub_date = request.POST["pub_date"]
		isbn = request.POST["isbn"]
		context["form_data"] = {
			"title": title,
			"author": author,
			"genre": genre,
			"pub_date": pub_date,
			"isbn": isbn,
		}

		isbn = isbn.strip()
		isbn = re.sub("^(?:ISBN(?:-1[03])?:? )?", "", isbn)

		def valid_isbn(s):
			if len(s) < 9 or len(s) > 17:
				return False
			s = s.replace(" ", "").replace("-","")

			if re.match("[^0-9]", s[:len(s) - 1]):
				return False
			if re.match("[^0-9]X", s[len(s) - 1]):
				return False

			chars = list(s)

			last = chars.pop()

			if len(chars) == 9:
				
				val = sum((x + 2) * int(y) for x, y in enumerate(reversed(chars)))
				check = 11 - (val % 11)
				if check == 10:
					check = "X"
				elif check == 11:
					check = "0"
			else:
				val = sum((x % 2 * 2 + 1) * int(y) for x, y in enumerate(chars))
				check = 10 - (val % 10)
				if check == 10:
					check = "0"

			return str(check) == last

		if isbn and not valid_isbn(isbn):
			context["message"] = "Invalid ISBN."
			return render(request, "new_book.html", context)

		book_exist = False
		try:
			Book.objects.get(title=title, author=author)
			book_exist = True
		except:
			pass
		if not book_exist:
			book = Book.objects.create(
				title=title, author=author, genre=genre, pub_date=pub_date, isbn=isbn
			)
		else:
			context["message"] = "Book already exists."
			return render(request, "new_book.html", context)
		nav = request.POST.get("submit")
		if nav == "go_home":
			return HttpResponseRedirect("/index")
		if nav == "see_all":
			return HttpResponseRedirect("/books")
	return render(request, "new_book.html")


def all_books(request):
	filtered_books = cache.get("filtered_books")
	if not filtered_books:
		filtered_books = Book.objects.all()
		cache.set("filtered_books", filtered_books)
	if request.method == "GET":
		books = Book.objects.all()
		context = {"all_books": books}
		cache.set("filtered_books", books)
		return render(request, "all_books.html", context)
	elif request.method == "POST":
		books = Book.objects.all()
		title_filter = request.POST["title_filter"]
		if title_filter:
			books = books.filter(title__contains=title_filter)
		author_filter = request.POST["author_filter"]
		if author_filter:
			books = books.filter(author__contains=author_filter)
		genre_filter = request.POST["genre_filter"]
		if genre_filter:
			books = books.filter(genre__contains=genre_filter)
		start_date = request.POST["start_date"]
		if start_date:
			books = books.filter(pub_date__gt=start_date)
		end_date = request.POST["end_date"]
		if end_date:
			books = books.filter(pub_date__lt=end_date)

		cache.set("filtered_books", books)
		context = {"all_books": books}
		context["filter_data"] = {
			"title": title_filter,
			"author": author_filter,
			"genre": genre_filter,
			"start_date": start_date,
			"end_date": end_date,
		}
		return render(request, "all_books.html", context)


def download(request):
	response = HttpResponse(content_type="text/csv")
	response["Content-Disposition"] = 'attachment; filename="books.csv"'

	writer = csv.writer(response)
	writer.writerow(
		["Entry ID", "Title", "Author", "Genre", "Publication Date", "ISBN"]
	)
	books = cache.get("filtered_books")
	if not books:
		books = Book.objects.all()
	for book in books:
		writer.writerow(
			[
				book.entry_id,
				book.title,
				book.author,
				book.genre,
				book.pub_date,
				book.isbn,
			]
		)

	return response
