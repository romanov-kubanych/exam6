from django.shortcuts import render, redirect

from webapp.forms import BookForm
from webapp.models import Book


def index_view(request):
    books = Book.objects.all().filter(status='active').order_by('-created_at')
    return render(request, 'index_view.html', {'books': books})


def create_book_view(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book_create.html', {"form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            new_book = Book.objects.create(author=author, email=email, text=text)
            books = Book.objects.all().filter(status='active').order_by('-created_at')
            return render(request, 'index_view.html', {'books': books})
        return render(request, 'book_create.html', {"form": form})
