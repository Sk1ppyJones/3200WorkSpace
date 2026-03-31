from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from blogapp.forms import CommentForm
from .models import Post

# Create your views here.


def starting_page(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})


def posts(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'posts.html', {'posts': posts})


class post_detail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.all().order_by('-created_date')
        form = CommentForm()
        stored_posts = request.session.get('stored_posts', [])

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comment_form': form,
                'comments': comments,
                'saved_for_later': post.id in stored_posts,
            },
        )

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        comments = post.comments.all().order_by('-created_date')

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-details', slug=slug)

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comment_form': comment_form,
                'comments': comments,
                'saved_for_later': post.id in request.session.get('stored_posts', []),
            },
        )


class read_later(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts', [])
        context = {
            'posts': Post.objects.filter(id__in=stored_posts).order_by('-published_date'),
            'has_posts': len(stored_posts) > 0,
        }
        return render(request, 'read-later.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts', [])
        post_id = request.POST.get('post_id')
        redirect_url = request.POST.get('next')

        if post_id is None:
            return redirect('read-later')

        post_id = int(post_id)

        if post_id in stored_posts:
            stored_posts.remove(post_id)
        else:
            stored_posts.append(post_id)

        request.session['stored_posts'] = stored_posts

        if redirect_url and redirect_url.startswith('/'):
            return redirect(redirect_url)

        return redirect('read-later')

class post_create(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'tags', 'image']
    template_name = 'post_create.html'
    success_url = '/posts'