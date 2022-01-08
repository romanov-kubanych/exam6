from django.urls import path

from webapp.views import index_view, create_book_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('book/add/', create_book_view, name='create_view')
]
