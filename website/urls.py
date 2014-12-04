from django.conf.urls import patterns, url


urlpatterns = patterns(
    'website.views',
    url(r'^$', 'home', name='home_url'),
)
