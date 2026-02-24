import csv
from django.core.management.base import BaseCommand
from readinglogApp.models import Book, Author, Genre, AuthorProfile


class Command(BaseCommand):
    help = 'Imports relational data while respecting One-to-One constraints'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # 1. Handle Genre
                    genre_obj, _ = Genre.objects.get_or_create(
                        name=row['genre'])

                    # 2. Handle Authors
                    author_list = []
                    names = row['authors'].split(',')

                    for name in names:
                        name = name.strip()
                        parts = name.split(' ', 1)
                        f_name = parts[0]
                        l_name = parts[1] if len(parts) > 1 else ""

                        # Check if Author exists first to avoid profile conflicts
                        author_obj, a_created = Author.objects.get_or_create(
                            first_name=f_name,
                            last_name=l_name
                        )

                        # 3. Handle Profile ONLY if the Author was just created
                        # or if they don't have a profile yet
                        if not hasattr(author_obj, 'profile') or author_obj.profile is None:
                            profile_obj = AuthorProfile.objects.create(
                                bio=row['bio'],
                                website=row['website']
                            )
                            author_obj.profile = profile_obj
                            author_obj.save()

                        author_list.append(author_obj)

                    # 4. Handle Book
                    book, b_created = Book.objects.get_or_create(
                        title=row['title'],
                        defaults={
                            'rating': int(row['rating']),
                            'is_read': row['is_read'].lower() == 'true',
                            'genre': genre_obj
                        }
                    )

                    # 5. Link Many-to-Many
                    for author in author_list:
                        book.authors.add(author)

                    self.stdout.write(self.style.SUCCESS(
                        f"Processed: {book.title}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
