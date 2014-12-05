from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'blogs', name='blogs_url'),
    url(r'^([^/]+)$', 'blog', name='blog_url'),
    url(r'^([^/]+)/(\d+)/([^/]+)$', 'blog_post', name='blog_post_url'),
)
