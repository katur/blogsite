from django.conf.urls import patterns, url


urlpatterns = patterns(
    'website.views',
    url(r'^$', 'home', name='home_url'),
)

urlpatterns += patterns(
    '',
    url(
        r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login_url'),
    url(
        r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout_url'),
)
