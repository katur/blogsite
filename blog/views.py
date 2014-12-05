from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blogsite.settings import (BLOG_POSTS_PER_PAGE,
                               BLOG_POST_TRUNCATION_FACTOR)
from blog.models import Blog, Post, PostView


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def blog(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    all_posts = Post.objects.filter(blog=blog)
    paginator = Paginator(all_posts, BLOG_POSTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        display_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an int, default to first page
        display_posts = paginator.page(1)
    except EmptyPage:
        # If out of range, default to last page
        display_posts = paginator.page(paginator.num_pages)

    context = {
        'blog': blog,
        'posts': display_posts,
        'truncation_factor': BLOG_POST_TRUNCATION_FACTOR}
    return render(request, 'blog.html', context)


def blog_post(request, blog_slug, post_id, post_slug):
    post = get_object_or_404(Post, blog__slug=blog_slug,
                             id=post_id, slug=post_slug)
    record_post_view(request, post)
    context = {'post': post}
    return render(request, 'post.html', context)


def record_post_view(request, post):
    """Record the post view if it is the first of its session."""
    if not request.session.get('has_session'):
        request.session['has_session'] = True

    session_key = request.session.session_key

    if not PostView.objects.filter(post=post, session_key=session_key):
        post_view = PostView(post=post,
                             ip=request.META['REMOTE_ADDR'],
                             time_created=timezone.now(),
                             session_key=session_key)
        post_view.save()
