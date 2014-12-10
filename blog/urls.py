from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'blogs', name='blogs_url'),
    url(r'^new-post$', 'new_blog_post', name='new_blog_post_url'),
    url(r'^edit/(\d+)/([^/]+)$', 'edit_blog_post', name='edit_blog_post_url'),
    url(r'^([^/]+)$', 'blog', name='blog_url'),
    url(r'^([^/]+)/(\d+)/([^/]+)$', 'blog_post', name='blog_post_url'),
)
