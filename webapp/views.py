from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import BookForm
from webapp.models import Book


def index_view(request):
    form = BookForm()
    books = Book.objects.all().filter(status='active').order_by('-created_at')
    return render(request, 'index_view.html', {'books': books, 'form': form})


def create_book_view(request):
    if request.method == 'GET':
        return redirect('index_view')
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            new_book = Book.objects.create(author=author, email=email, text=text)
            return redirect('index_view')
        return redirect('index_view')


def update_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={
            'author': book.author,
            'email': book.email,
            'text': book.text
        })
        return render(request, 'book_update.html', {'form': form, 'book': book})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.author = form.cleaned_data.get('author')
            book.email = form.cleaned_data.get('email')
            book.text = form.cleaned_data.get('text')
            book.save()
            return redirect('index_view')
        return render(request, 'book_update.html', {'form': form, 'book': book})


def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'book_delete.html', {'book': book})
    else:
        book.delete()
        return redirect('index_view')
