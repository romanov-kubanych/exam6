from django.urls import path

from webapp.views import index_view, create_book_view, update_book_view, delete_book_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('book/add/', create_book_view, name='create_view'),
    path('book/<int:pk>/update/', update_book_view, name='update_view'),
    path('book/<int:pk>/delete/', delete_book_view, name='delete_view')
]
