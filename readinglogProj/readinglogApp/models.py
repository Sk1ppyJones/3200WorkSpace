from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    bio = models.TextField()
    website = models.URLField(null=True)

    # THIS WILL BREAK
    def __str__(self):
        if hasattr(self, 'author'):
            return f"Profile for {self.author}"
        else:
            return "Unassigned Profile"


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField('', null=False, db_index=True, blank=True)
    profile = models.OneToOneField(
        AuthorProfile, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + '-' + self.last_name)
        super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=128)
    rating = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)])

    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    authors = models.ManyToManyField(Author, related_name="books")
    is_read = models.BooleanField(default=False)
    date_read = models.DateField(null=True)
    series_number = models.IntegerField(null=True)
    summary = models.CharField(max_length=500, null=True)
    slug = models.SlugField(default='', null=False,
                            db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f"{self.title} - ({self.rating}/5)"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
