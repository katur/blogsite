from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Post


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def blog(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog)
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blog.html', context)


def blog_post(request, blog_slug, post_id, post_slug):
    post = get_object_or_404(Post, blog__slug=blog_slug,
                             id=post_id, slug=post_slug)
    context = {'post': post}
    return render(request, 'post.html', context)
