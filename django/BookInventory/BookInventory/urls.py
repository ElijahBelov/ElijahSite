"""BookInventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.templatetags.static import static
import Books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", Books.views.index, name="index"),
    path("", Books.views.home),
    path("home/", Books.views.home, name="home"),
    path("new_book/", Books.views.new_book, name="new_book"),
    path("books/", Books.views.all_books, name="all_books"),
    path("books/download", Books.views.download, name="download_books"),
]
