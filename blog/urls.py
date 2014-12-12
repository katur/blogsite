from django.conf.urls import patterns, url
from blog.feeds import AllPostsFeed


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'blogs', name='blogs_url'),
    url(r'^new-post$', 'new_blog_post', name='new_blog_post_url'),
    url(r'^upload-image$', 'upload_image', name='upload_image_url'),
    url(r'^edit/(\d+)/([^/]+)$', 'edit_blog_post', name='edit_blog_post_url'),
    url(r'^([^/]+)$', 'blog', name='blog_url'),
    url(r'^([^/]+)/(\d+)/([^/]+)$', 'blog_post', name='blog_post_url'),
)

urlpatterns += patterns('', url(r'^(?P<blog_slug>[^/]+)/rss$',
                        AllPostsFeed(), name='blog_rss_url'))
