from math import log

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Blog, Post, PostView
from blog.forms import PostForm, UploadImageForm
from taggit.models import Tag, TaggedItem

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
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def blog(request, blog_slug):
    """Render the landing page for a single blog.

    A list of posts is shown. These posts may be filtered by various
    user-selected filters (e.g. by tag, author). In addition,
    any draft or post scheduled for future publication show up for
    the post's author only.
    """
    blog = get_object_or_404(Blog, slug=blog_slug)

    if request.user.is_authenticated():
        posts = get_visible_posts(blog, request.user)

    else:
        posts = get_visible_posts(blog)

    # Get tag cloud for all viewable posts, before applying filters
    tag_cloud = get_tag_cloud(posts=posts)

    if 'author' in request.GET:
        author = get_object_or_404(User, username=request.GET.get('author'))
        posts = posts.filter(author=author)

    if 'tag' in request.GET:
        tag = get_object_or_404(Tag, slug=request.GET.get('tag'))
        posts = posts.filter(tags__in=[tag])

    num_filtered = len(posts)

    paginator = Paginator(posts, BLOG_POSTS_PER_PAGE)
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
        'num_filtered': num_filtered,
        'truncation_factor': BLOG_POST_TRUNCATION_FACTOR,
        'tag_cloud': tag_cloud,
    }

    return render(request, 'blog.html', context)


def blog_post(request, blog_slug, post_id, post_slug):
    """Render the page displaying a single post."""
    post = get_object_or_404(Post, blog__slug=blog_slug,
                             id=post_id, slug=post_slug)
    if not post.is_published or post.is_future_publication():
        if not request.user.is_authenticated() or request.user != post.author:
            raise Http404

    record_post_view(request, post)
    context = {'post': post}
    return render(request, 'post.html', context)


@login_required
def new_blog_post(request):
    """Render the page to create a new post."""
    current_user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # TODO: I think this check is overkill, but maybe good to have
            if (current_user != form.cleaned_data['author'] or
                    current_user not in
                    form.cleaned_data['blog'].authors.all()):
                raise Http404
            return save_post_and_redirect(form, request)

    else:
        blogs = Blog.objects.filter(authors__in=[current_user])

        if 'blog' in request.GET:
            blog = get_object_or_404(Blog, slug=request.GET.get('blog'))
            if blog not in blogs:
                blog = None
        else:
            blog = None

        form = PostForm(initial={'blog': blog, 'author': current_user})
        form.fields['author'].widget = forms.HiddenInput()
        form.fields['blog'].queryset = blogs

    context = {'form': form}
    return render(request, 'new_post.html', context)


@login_required
def edit_blog_post(request, post_id, post_slug):
    """Render the page edit an existing post."""
    post = get_object_or_404(Post, id=post_id, slug=post_slug)
    current_user = request.user

    # Only the author can edit the post, and the author must still be listed
    # as a contributor.
    if (current_user != post.author or
            current_user not in post.blog.authors.all()):
        raise Http404

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            return save_post_and_redirect(form, request)

    else:
        form = PostForm(instance=post)
        form.fields['author'].widget = forms.HiddenInput()

        # Limit blogs dropdown to those the current user can edit
        blogs = Blog.objects.filter(authors__in=[current_user])
        form.fields['blog'].queryset = blogs

    context = {'form': form, 'post': post}
    return render(request, 'edit_post.html', context)


@login_required
def upload_image(request):
    if 'image' in request.GET:
        image = request.GET.get('image')
        context = {'image': image}

    elif request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            redirect_url = "{}?image={}".format(
                reverse('blog.views.upload_image'), image.image.name)
            return HttpResponseRedirect(redirect_url)
    else:
        form = UploadImageForm(initial={'user': request.user})
        form.fields['user'].widget = forms.HiddenInput()
        context = {'form': form}

    return render(request, 'upload_image.html', context)


####################
# HELPER FUNCTIONS #
####################
def get_visible_posts(blog, user=None):
    """
    Get all posts for this blog that are visible to the user.

    If no user provided, limits to posts already published.

    If a user is provided, any non-public posts authored by that user (drafts,
    or posts scheduled for future publication) are included too.
    """
    if user:
        return Post.objects.filter(
            Q(blog=blog) &
            (Q(author=user) |
             (Q(is_published=True) & Q(time_published__lte=timezone.now()))))
    else:
        return Post.objects.filter(Q(blog=blog) &
                                   Q(is_published=True) &
                                   Q(time_published__lte=timezone.now()))


def save_post_and_redirect(form, request):
    if 'publish' in request.POST:
        post = form.save(publish=True)
        return HttpResponseRedirect(
            reverse('blog.views.blog_post',
                    args=[post.blog.slug, post.id, post.slug]))
    else:
        post = form.save()
        return HttpResponseRedirect(
            reverse('blog.views.edit_blog_post',
                    args=[post.id, post.slug]))


def record_post_view(request, post):
    """Record in the database that a post was viewed.

    Only records post views if they haven't occurred in the same session.
    """
    if not request.session.get('has_session'):
        request.session['has_session'] = True

    session_key = request.session.session_key

    if not PostView.objects.filter(post=post, session_key=session_key):
        post_view = PostView(post=post,
                             ip=request.META['REMOTE_ADDR'],
                             time_created=timezone.now(),
                             session_key=session_key)
        post_view.save()


def get_tag_cloud(posts=None, count_threshold=0, max_size=2.0, min_size=.6):
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

    if posts:
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
