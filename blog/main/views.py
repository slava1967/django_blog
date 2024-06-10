from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post, Category


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def index(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    return render(request, 'main/index.html', {'posts': posts})


def single_post(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'main/post_detail.html', {'post': post, 'form': form})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | Q(body__icontains=query))

    return render(request, 'main/search.html', {'posts': posts, 'query': query})


def contact(request):
    return render(request, 'main/contact.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /slava1967/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
