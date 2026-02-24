from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating')
    # books = books_raw.filter(author="David Baldacci")

    avg_rating = books.aggregate(Avg('rating'))
    num_books = books.count()

    return render(request, 'readinglogApp/index.html', {"books": books, "average": avg_rating, "bookcount": num_books})


def book_detail(request, slug):
    try:
        print(Book.objects.get(slug=slug))
        # book = Book.objects.get(slug=slug)
        book = get_object_or_404(Book, slug=slug)

    except:
        raise Http404()

    author_names = ", ".join([author.full_name()
                             for author in book.authors.all()])

    return render(request, 'readinglogApp/book_detail.html', {
        'title': book.title,
        'author': author_names,
        'series_number': book.series_number,
        'date_read': book.date_read,
        'is_read': book.is_read,
        'rating': book.rating,
        'summary': book.summary
    })
