from django.shortcuts import render

from webapp.models import Book


def index_view(request):
    books = Book.objects.all().filter(status='active').order_by('-created_at')
    return render(request, 'index_view.html', {'books': books})

