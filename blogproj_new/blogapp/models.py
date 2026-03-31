from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first} {self.last}"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            candidate = base_slug
            n = 1
            while Post.objects.filter(slug=candidate).exists():
                candidate = f"{base_slug}-{n}"
                n += 1
            self.slug = candidate
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post.title}"