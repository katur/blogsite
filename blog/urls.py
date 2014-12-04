from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'posts', name='posts_url'),
)
