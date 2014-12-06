from math import log

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Blog, Post, PostView
from taggit.models import TaggedItem

try:
    from django.conf.settings import BLOG_POSTS_PER_PAGE
except ImportError:
    BLOG_POSTS_PER_PAGE = 10

try:
    from django.conf.settings import BLOG_POST_TRUNCATION_FACTOR
except ImportError:
    BLOG_POST_TRUNCATION_FACTOR = 500


def blogs(request):
    """Render the page listing all blogs."""
    blogs = Blog.objects.all()
    tag_cloud = get_tag_cloud()
    context = {'blogs': blogs, 'tag_cloud': tag_cloud}
    return render(request, 'blogs.html', context)


def blog(request, blog_slug):
    """Render the landing page for a single blog."""
    blog = get_object_or_404(Blog, slug=blog_slug)
    all_posts = Post.objects.filter(blog=blog)
    tag_cloud = get_tag_cloud(blog=blog)

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
        'truncation_factor': BLOG_POST_TRUNCATION_FACTOR,
        'tag_cloud': tag_cloud,
    }

    return render(request, 'blog.html', context)


def blog_post(request, blog_slug, post_id, post_slug):
    """Render the page displaying a single post."""
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


def get_tag_cloud(count_threshold=0, max_size=2.0, min_size=.6, blog=None):
    """Get the tags along with their relative sizes for 'tag cloud'.

    Tags are only displayed if their count is above threshold.
    max_size and min_size determine the range of the CSS font-size
    for tags.

    The math is by http://dburke.info/blog/logarithmic-tag-clouds/
    """
    def tally(tag, tag_with_counts):
        if tag not in tags_with_counts:
            tags_with_counts[tag] = 0
        tags_with_counts[tag] += 1

    tags_with_counts = {}
    tag_cloud = []

    if blog:
        posts = Post.objects.filter(blog=blog)
        for post in posts:
            for tag in post.tags.all():
                tally(tag, tags_with_counts)

    else:
        tagged_items = TaggedItem.objects.all()
        for tagged_item in tagged_items:
            tally(tagged_item.tag, tags_with_counts)

    if not tags_with_counts:
        return tag_cloud

    min_count = min(tags_with_counts.itervalues())
    max_count = max(tags_with_counts.itervalues())
    constant = log(max_count - (min_count-1))/(max_size - min_size or 1)

    for tag, count in tags_with_counts.iteritems():
        if count >= count_threshold:
            size = log(count - (min_count-1))/(constant or 1) + min_size
            tag_cloud.append({
                'tag': tag,
                'size': round(size, 7)
            })

    return tag_cloud
