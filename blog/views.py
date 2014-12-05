from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Post


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def blog(request, blog_slug):
    posts = Post.objects.filter(blog__slug=blog_slug).order_by('-time_created')
    context = {'posts': posts}
    return render(request, 'blog.html', context)


def blog_post(request, blog_name, post_id, post_slug):
    post = get_object_or_404(Post, blog__name=blog_name,
                             id=post_id, slug=post_slug)
    context = {'post': post}
    return render(request, 'post.html', context)
