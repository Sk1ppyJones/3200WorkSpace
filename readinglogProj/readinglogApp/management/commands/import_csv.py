import csv
from django.core.management.base import BaseCommand
from readinglogApp.models import Book


class Command(BaseCommand):
    help = 'Imports book data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    is_read_bool = row['is_read'].lower() == 'true'
                    obj, created = Book.objects.get_or_create(
                        title=row['title'],
                        defaults={
                            'authors': row['authors'],
                            'rating': int(row['rating']),
                            'is_read': is_read_bool
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(
                            f"Imported: {row['title']}"))
                    else:
                        self.stdout.write(self.style.WARNING(
                            f"Skipped: {row['title']}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
