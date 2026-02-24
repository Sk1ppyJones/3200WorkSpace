from django.contrib import admin
from .models import Author, Tag, Post

# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
