from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'', include('website.urls')),
    url(r'^blog/', include('blog.urls')),
    # Examples:
    # url(r'^$', 'blogsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
