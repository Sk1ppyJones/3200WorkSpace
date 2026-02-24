from django.contrib import admin
from .models import Book, Genre, Author, AuthorProfile

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    # prepopulated_fields = {'slug': ('title')}
    # list_filter = ('author', 'rating', 'is_read')
    # list_display = ('author', 'is_read')
    # search_fields = ('title',)


admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(AuthorProfile)
