from django.contrib import admin

from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'status']
    list_filter = ['author']
    search_fields = ['status', 'email']
    fields = ['author', 'email', 'text', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Book, BookAdmin)
