from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def starting_page(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})


def posts(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request):
    # expect a `slug` parameter from the URL
    slug = request.resolver_match.kwargs.get('slug')
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
